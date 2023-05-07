import { createRouter, createWebHistory } from 'vue-router'
import HomePage from "./components/HomePage"
import MessageRead from "./components/MessageRead"
import ExperienceModule from "./components/ExperienceModule"
const routes = [
    { path: '/', name: "home", component: HomePage },
    { path: '/messages', component: MessageRead },
    { path: '/experience', component: ExperienceModule},
    { path: '/sign-in', component: () => import("./components/SignIn")},
    { path: '/register', component: () => import("./components/RegisterUser")}
  ]
  export const router = createRouter({
    history: createWebHistory(),
    routes,
  })

  export default router