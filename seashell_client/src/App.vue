<template>
  <NavBar></NavBar>
  <router-view class="app-body"></router-view>
  <!-- <MessageRead></MessageRead>
  <ComposeMessage></ComposeMessage> -->
  <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
  <AppFooter></AppFooter>

</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import { RouterView } from "vue-router";
import NavBar from "./components/NavBar.vue"
import AppFooter from "./components/AppFooter.vue";
// import MessageRead from "./components/MessageRead.vue";
// import ComposeMessage from "./components/ComposeMessage.vue";
import '@coreui/coreui/dist/css/coreui.min.css'
import axios from "axios";
export const client = axios.create({
  baseURL: "http://127.0.0.1:8000"
})
export default {
  name: 'App',
  components: {
    // HelloWorld,
    // MessageRead,
    // ComposeMessage,
    NavBar,
    RouterView,
    AppFooter
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