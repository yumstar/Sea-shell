<template>
    <div class="input-field">
        <span class="p-float-label">
                <Textarea id="message" v-model="value" type="text" :class="{ 'p-invalid': errorMessage }" aria-describedby="text-error" />
                <label for="message">Message</label>
        </span>
        <small class="p-error" id="text-error">{{ errorMessage || '&nbsp;' }}</small>
    </div>
</template>

<script setup>
import { useField } from 'vee-validate';
import Textarea from 'primevue/textarea'
const { value, errorMessage } = useField('message', validateMessage);

function validateMessage(value) {
    if (!value) {
        return 'Please enter the affirmation you would like to write.';
    }

    return true;
}
</script>

<style lang="scss" scoped>
.input-field{
    padding-top: 2em;
}
</style>