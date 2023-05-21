<template>
    <div class="message-block">
        {{props.body}}
        <div class="message-tags p-3">
        <Chip v-for="tag in tags" :key="tag">{{ tag }}</Chip>  
        </div>
    </div>
</template>

<script setup>
import { defineProps} from 'vue';
import Chip from 'primevue/chip';
const props = defineProps({
    body: String,
    tags: Array
})
</script>

<style lang="scss" scoped>
.message-block{
    display: inline;
    width: fit-content;
    height: fit-content;
    margin: 1em;
    border-radius: var(--border-radius);
    box-shadow: -4px 3px 47px -2px rgba(232,228,228,0.75);
-webkit-box-shadow: -4px 3px 47px -2px rgba(232,228,228,0.75);
-moz-box-shadow: -4px 3px 47px -2px rgba(232,228,228,0.75);
}

</style>