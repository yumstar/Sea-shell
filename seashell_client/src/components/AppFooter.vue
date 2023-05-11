<template>
    <div class="footer">
        <a href="https://www.flaticon.com/free-icons/seashell" title="seashell icons">Seashell icons created by Freepik - Flaticon</a>
        <Button type="button" label="sign-out" @click="authStatusStore.signOut()">Sign Out</Button>
    </div>
</template>

<script setup>
import Button from 'primevue/button';
import { useAuthStatusStore } from "@/stores/authStatus";
const authStatusStore = useAuthStatusStore();
</script>

<style lang="scss" scoped>
.footer{
    // position: absolute;
    display: flex;
    top: 100%;
    flex-direction: row;
}


</style>