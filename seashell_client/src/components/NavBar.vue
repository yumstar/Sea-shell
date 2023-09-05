<template>
    <div>
        <Menubar :model="items">
            <template #item="slotProps">
                <router-link :to="slotProps.item.link" class="nav-item">
                    {{ slotProps.item.label}}
                </router-link>
            </template>
            <template #start>
                <img alt="logo" src="../assets/logo-nobg.png" id="app-logo" draggable="false" class="max-h-20 max-w-20 mx-auto"/>
            </template>
        </Menubar>
    </div>
</template>

<script setup>
// import { CNavbar, CNavbarBrand, CContainer, CNavbarNav, CNavItem} from '@coreui/vue'
import { ref } from 'vue';
import Menubar from 'primevue/menubar';
// import NavItem from './NavItem.vue';
import { RouterLink } from 'vue-router';
const items = ref([
    {
        label: "Home",
        link: "/"
    },
    {
        label: "Read",
        link: "/messages"
    },
    // {
    //     label: "Day",
    //     link: "/experience"
    // }
])
</script>

<style lang="scss" scoped>
// @import url('https://fonts.googleapis.com/css2?family=Barlow+Semi+Condensed:wght@500&display=swap');
#app-logo {
    // height: 2em;
    user-select: none;
}
h1 {
    font-family: 'Barlow Semi Condensed';
}
a.nav-item {
    margin-left: 2em;
    margin-right: 1em;
    font-size: 1.5em;
    font-family: 'Barlow Semi Condensed';
    text-decoration: none;
    color: grey;
}


.p-menubar{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    background-color: white;
    border: none;
}
@font-face {
    font-family: 'Barlow Semi Condensed';
    src: url('../assets/fonts/BarlowSemiCondensed-Medium.ttf') format("truetype");
}

</style>