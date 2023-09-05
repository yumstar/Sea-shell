import { defineStore } from 'pinia'
import {computed, ref} from "vue"
import axios from 'axios'
import { client } from '@/App'
import { app } from '@/main'
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.withCredentials = true;
export const useAuthStatusStore = defineStore('authStatus',() => {
    const $cookies = app.$cookies
    const isAuthenticated = ref($cookies.get('token') && $cookies.get('token').length > 0)
    const token = ref($cookies.get('token'))
    const getToken = computed(() => token.value) 
    const getIsAuthenticated = computed(() => isAuthenticated.value)
    var url
    if (process.env.VUE_APP_STAGE == 'prod'){
        url = process.env.VUE_APP_LAMBDA_ENDPOINT + "api/centerUser/"
      }
      else{
        url = "http://127.0.0.1:8000/api/centerUser/"
      } 
    if(getToken.value && getToken.value.length > 0) {
        client.defaults.headers['Authorization'] = `Token ${getToken.value}`
    }
    const authUrl = ref(url) 
    async function signOut() {
        try {
            // await axios.post(authUrl.value + "signout", {}, {withCredentials: true, xsrfCookieName: 'csrftoken', xsrfHeaderName: 'X-CSRFToken'})
            await axios.post(authUrl.value + "signout", {}, {withCredentials: true})
            // $cookies.remove('csrftoken')
            $cookies.remove('token')
            token.value = ''
            isAuthenticated.value = false  
        }
        catch {
            // $cookies.remove('sessionid')
            // $cookies.remove('csrftoken')
            $cookies.remove('token')
            throw Error("Error signing out.")
        }
    }
    async function signIn(creds) {
        try{
            // $cookies.remove('sessionid')
            // $cookies.remove('csrftoken')
            const res = await axios.post(authUrl.value + "signin",  creds, {})
            const data = res.data
            $cookies.set("token", data.token)
            token.value = $cookies.get('token')
            client.defaults.headers.common['Authorization'] = `Token ${getToken.value}`
            isAuthenticated.value = true
        }
        catch(error) {
            // throw Error("Error signing in.")
            throw Error(error) 
        }
    }
    return {isAuthenticated, token, getToken, getIsAuthenticated, signIn, signOut}
})