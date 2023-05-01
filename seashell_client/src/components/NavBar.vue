<template>
    <div>
        <Menubar :model="items">
            <template #item="slotProps">
                <router-link :to="slotProps.item.link" class="nav-item">
                    {{ slotProps.item.label}}
                </router-link>
            </template>
            <template #start>
                <img alt="logo" src="../assets/seashell.png" id="app-logo" draggable="false"/>
                <h1> Seashell</h1>
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
    {
        label: "Day",
        link: "/experience"
    }
])
</script>

<style lang="scss" scoped>
// @import url('https://fonts.googleapis.com/css2?family=Barlow+Semi+Condensed:wght@500&display=swap');
#app-logo {
    height: 2em;
    user-select: none;
}
h1 {
    font-family: 'Barlow Semi Condensed';
}
a.nav-item {
    margin-left: 2em;
    margin-right: 1em;
    font-size: 1.5em;
    // border: 2px solid black;
    font-family: 'Barlow Semi Condensed';
    // a {
    text-decoration: none;
    color: grey;
    // }
    :hover  {
        color: black;
    }
}


.p-menubar{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    background-color: white;
    border: none;

}

.p-menubar-start{
        display: flex;
        flex-direction: row;
        width: 100%;
        border: 1px solid black;
        display: none;    
}

.p-menubar-root-list {
    border: 2px solid black;
    // width: 90%;
    display: flex;
    flex-direction: row;
}
@font-face {
    font-family: 'Barlow Semi Condensed';
    src: url('../assets/fonts/BarlowSemiCondensed-Medium.ttf') format("truetype");
}

</style>