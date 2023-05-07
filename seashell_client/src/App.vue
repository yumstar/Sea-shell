<template>
  <div class="app" @signout="() => {}">
  <NavBar></NavBar>
  <router-view class="app-body"></router-view>
  <AppFooter></AppFooter>
</div>
</template>

<script>
import { RouterView} from "vue-router";
import NavBar from "./components/NavBar.vue"
import AppFooter from "./components/AppFooter.vue";
import '@coreui/coreui/dist/css/coreui.min.css'
import axios from "axios";
import { reactive, inject, watch} from "vue";
import { router } from "./router.js"
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.withCredentials = true;

export const client = axios.create({
  baseURL: "http://127.0.0.1:8000"
})
const state = reactive({authenticated: false, token: null})
router.beforeEach(async (to) => {
  if((to.path === '/' || to.path === '/register')){
    return true
  }
  if(!state.authenticated && to.path !== '/sign-in'){
    return {path: "/sign-in"}
  }
})

const toggleAuthentication = () => {
  state.authenticated = state.token? true: false
}

const signOut = () => {
  client.post("api/centerUser/signout",  {withCredentials: true}).then(() => {
    const $cookies = inject('$cookies')
    $cookies.remove('csrftoken')
    state.token = null
  })
}
watch(state, toggleAuthentication)
export default {
  name: 'App',
  components: {
    NavBar,
    RouterView,
    AppFooter
},
  setup() {
    const $cookies = inject('$cookies')
    state.token = $cookies.get('csrftoken')
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Questrial&display=swap');
#app {
  font-family: (--font-family);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 30px;
  font-family: 'Questrial';
}
.app-body {
  min-height: 100vh;
  height: 100%;
}
@font-face {
    font-family: 'Barlow Semi Condensed';
    src: url('./assets/fonts/BarlowSemiCondensed-Medium.ttf') format("truetype");
}
</style>