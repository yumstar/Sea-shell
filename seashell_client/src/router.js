import { createRouter, createWebHistory } from 'vue-router'
import HomePage from "./components/HomePage"
import MessageRead from "./components/MessageRead"
import ExperienceModule from "./components/ExperienceModule"
const routes = [
    { path: '/', name: "home", component: HomePage },
    { path: '/messages',name: "messages", component: MessageRead },
    { path: '/experience', name: "experiences", component: ExperienceModule},
    { path: '/sign-in', name: "sign-in", component: () => import("./components/SignIn")},
    { path: '/register', name: "register", component: () => import("./components/RegisterUser")}
  ]
  export const router = createRouter({
    history: createWebHistory(),
    routes,
  })

  export default router