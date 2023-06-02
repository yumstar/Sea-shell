<template>
    <div class="input-field">
        <span class="p-float-label">
            <Chips id="newTags" v-model="value" :class="{ 'p-invalid': errorMessage }" aria-describedby="chips-error" class="chips mx-auto"/>
            <label for="message">New Tags</label>
        </span>
        <small class="p-error" id="text-error">{{ errorMessage || '&nbsp;' }}</small>
    </div>
</template>

<script setup>
import { useField } from 'vee-validate';
import Chips from 'primevue/chips'
const { value, errorMessage } = useField('newTags', validateTag);
function validateTag() {
    // if (!value) {
    //     return 'Please enter the affirmation you would like to write.';
    // }

    return true;
}
</script>

<style lang="scss" scoped>
.input-field{
    padding-top: 1em;
    // width: 100%;

}
.chips{
    max-width: 25em;
    width: 25em;
}
</style>