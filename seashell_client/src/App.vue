<template>
  <div class="app-container flex flex-col min-h-screen">
  <NavBar></NavBar>
  <router-view class="app-body mt-5"></router-view>
  <AppFooter></AppFooter>
</div>
</template>

<script>
import { RouterView} from "vue-router";
import NavBar from "./components/NavBar.vue"
import AppFooter from "./components/AppFooter.vue";
import '@coreui/coreui/dist/css/coreui.min.css'
import axios from "axios";
import { router } from "./router.js"
import { useAuthStatusStore } from "@/stores/authStatus";
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.withCredentials = true;
var url;
if (process.env.VUE_APP_STAGE == 'prod'){
  url = process.env.VUE_APP_LAMBDA_ENDPOINT
}
else{
  url = "http://127.0.0.1:8000"
} 
export const client = axios.create({
  baseURL: url,
  xsrfCookieName: 'csrftoken',
  xsrfHeaderName: 'X-CSRFToken',
  withCredentials: true
})
router.beforeEach(async (to) => {
  const authStatusStore = useAuthStatusStore()
  if((to.name === 'home' || to.name === 'register')){
    return true
  }
  if(!authStatusStore.getIsAuthenticated && to.name !== 'sign-in'){
    return {path: "/sign-in"}
  }
})





export default {
  name: 'App',
  components: {
    NavBar,
    RouterView,
    AppFooter
},
  setup() {
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
  min-height: 100vh;
}
.app-body {
  min-height: 100vh;
  /* height: 100vh; */
  height: 100%;
}
@font-face {
    font-family: 'Barlow Semi Condensed';
    src: url('./assets/fonts/BarlowSemiCondensed-Medium.ttf') format("truetype");
}
</style>