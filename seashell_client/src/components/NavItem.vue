<template>
    <div>
        <router-link :to="props.link">
                     {{props.label}}           
        </router-link>
    </div>
</template>

<script setup>
import { defineProps} from 'vue';
const props = defineProps({
    label: String,
    link: String
})
</script>

<style lang="scss" scoped>

</style>