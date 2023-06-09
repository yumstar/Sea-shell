import { createApp } from 'vue'
import { createPinia } from 'pinia'
import PrimeVue from 'primevue/config';
import App from './App.vue'
import VueCookies from 'vue-cookies'
import './index.css'
// import { createRouter, createWebHistory } from 'vue-router'
import router from './router';
import "primevue/resources/themes/mira/theme.css"
import "primevue/resources/primevue.min.css";
import { CIcon } from '@coreui/icons-vue';
import  {cilMoodVeryGood, cilMoodGood, cilMeh, cilMoodBad, cilSad} from '@coreui/icons'

const icons = {
  cilMoodVeryGood,
  cilMoodGood,
  cilMeh,
  cilSad,
  cilMoodBad,

}
const pinia = createPinia()
export const app = createApp(App)
app.use(pinia)
app.use(router)
app.use(PrimeVue);
app.use(VueCookies, { expires: '7d'})
app.provide('icons', icons)
app.component('CIcon', CIcon)
app.mount('#app');
