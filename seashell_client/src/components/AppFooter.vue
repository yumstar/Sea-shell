<template>
    <div class="footer mt-auto">
        <!-- <a href="https://www.flaticon.com/free-icons/seashell" title="seashell icons">Seashell icons created by Freepik - Flaticon</a> -->
        <Button type="button" label="sign-out" @click="signOut()" class="mx-1 my-2">Sign Out</Button>
    </div>
</template>

<script setup>
import Button from 'primevue/button';
import { useAuthStatusStore } from "@/stores/authStatus";
const authStatusStore = useAuthStatusStore();

const signOut = async () => {
    await authStatusStore.signOut()
    location.reload()
}
</script>

<style lang="scss" scoped>
.footer{
    position: sticky;
    width: 100%;
    display: flex;
    // top: 100%;
    // bottom: 100%;
    flex-direction: row;
}


</style>