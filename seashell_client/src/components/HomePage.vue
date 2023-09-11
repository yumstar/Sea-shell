<template>
    <div class="max-w-lg mx-auto my-5">
        <div id="landing-page-home-title" class="mb-4">
            <span class="text-6xl">seashell affirmations</span>
            <span class="emoji d-block text-8xl my-4">🐚</span>
        </div>
        <div id="landing-page-home-sub-title" class="mb-8">
            <span class="text-3xl">a lifestyle support tool for you to group your affirmations and memorize them to navigate any life scenario. 🏄</span>
        </div>
        <div class="mb-8">
            <span class="text-xl">tag your affirmations by situation or feeling and re-visit them regularly to positively change the way you think.</span>
        </div>

        <Button><router-link class="text-sky-200 text-2xl" to="/messages">use now 🌊</router-link></Button>
        
        <!-- <span class="emoji d-block text-8xl mt-3">🏖️</span> -->

    </div>
</template>

<script setup>
// import { RouterLink } from 'vue-router';
import Button from 'primevue/button';
</script>

<style lang="scss" scoped>

</style>