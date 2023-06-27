import { defineStore } from 'pinia'
import {computed, ref} from "vue"
import axios from 'axios'
import { app } from '@/main'
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.withCredentials = true;
export const useAuthStatusStore = defineStore('authStatus',() => {
    const $cookies = app.$cookies
    const isAuthenticated = ref($cookies.get('csrftoken') && $cookies.get('csrftoken').length > 0)
    const token = ref($cookies.get('csrftoken'))
    const getToken = computed(() => token.value)
    const getIsAuthenticated = computed(() => isAuthenticated.value)
    var url
    if (process.env.VUE_APP_STAGE == 'prod'){
        url = process.env.VUE_APP_LAMBDA_ENDPOINT + "api/centerUser/"
      }
      else{
        url = "http://127.0.0.1:8000/api/centerUser/"
      } 
    const authUrl = ref(url) 
    async function signOut() {
        try {
            await axios.post(authUrl.value + "signout", {}, {withCredentials: true, xsrfCookieName: 'csrftoken', xsrfHeaderName: 'X-CSRFToken'})
            $cookies.remove('csrftoken')
            token.value = ''
            isAuthenticated.value = false  
        }
        catch {
            throw Error("Error signing out.")
        }
    }
    async function signIn(creds) {
        try{
            await axios.post(authUrl.value + "signin",  creds, {})
            token.value = $cookies.get('csrftoken')
            isAuthenticated.value = true
        }
        catch {
            throw Error("Error signing in.") 
        }
    }
    return {isAuthenticated, token, getToken, getIsAuthenticated, signIn, signOut}
})