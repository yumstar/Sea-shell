<template>
    <div class="input-field">
        <span class="p-float-label">
            <Chips v-model="value" :class="{ 'p-invalid': errorMessage }" aria-describedby="chips-error" class="chips"/>
            <label for="message">New Tags</label>
        </span>
        <small class="p-error" id="text-error">{{ errorMessage || '&nbsp;' }}</small>
    </div>
</template>

<script setup>
import { useField } from 'vee-validate';
import Chips from 'primevue/chips'
const { value, errorMessage } = useField('message', validateTag);
function validateTag(value) {
    if (!value) {
        return 'Please enter the affirmation you would like to write.';
    }

    return true;
}
</script>

<style lang="scss" scoped>
.input-field{
    padding-top: 1em;
}
.chips{
    max-width: 25em;
    // width: 25em;
}
</style>