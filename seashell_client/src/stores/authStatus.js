import { defineStore } from 'pinia'
import {computed, ref} from "vue"
import axios from 'axios'
import { app } from '@/main'
export const useAuthStatusStore = defineStore('authStatus',() => {
    const $cookies = app.$cookies
    const isAuthenticated = ref(false)
    const token = ref('')
    const getToken = computed(() => token.value)
    const getIsAuthenticated = computed(() => isAuthenticated.value)
    const authUrl = ref("http://127.0.0.1:8000/api/centerUser/") 
    async function signOut() {
        try {
            await axios.post(authUrl.value + "signout",  {withCredentials: true})
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
            await axios.post(authUrl.value + "signin",  creds)
            token.value = $cookies.get('csrftoken')
            isAuthenticated.value = true
        }
        catch {
            throw Error("Error signing in.") 
        }
    }
    return {isAuthenticated, token, getToken, getIsAuthenticated, signIn, signOut}
})