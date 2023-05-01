import { createApp } from 'vue'
import PrimeVue from 'primevue/config';
import App from './App.vue'
import HomePage from "./components/HomePage"
import MessageRead from "./components/MessageRead"
import ExperienceModule from "./components/ExperienceModule"
import { createRouter, createWebHistory } from 'vue-router'
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
const routes = [
    { path: '/', component: HomePage },
    { path: '/messages', component: MessageRead },
    { path: '/experience', component: ExperienceModule}
  ]
const router = createRouter({
    history: createWebHistory(),
    routes,
  })

const app = createApp(App)
app.use(router)
app.use(PrimeVue);
app.provide('icons', icons)
app.component('CIcon', CIcon)
app.mount('#app');
