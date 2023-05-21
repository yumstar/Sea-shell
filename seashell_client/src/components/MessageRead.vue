<template>
    <Suspense>
        <MessageBoard></MessageBoard>
        <template #fallback>
            <ProgressSpinner style="width: 50px; height: 50px" strokeWidth="8" fill="var(--surface-ground)"
    animationDuration=".5s" aria-label="Custom ProgressSpinner" />
        </template>
    </Suspense>
    <MessageComposer></MessageComposer>
</template>

<script setup>
import MessageComposer from './MessageComposer.vue';
import MessageBoard from './MessageBoard.vue';
import ProgressSpinner from 'primevue/progressspinner';


</script>

<style lang="scss" scoped>

</style>