<template>
    <div class="input-field">
        <span class="p-float-label">
                <InputText id="email" v-model="value" type="email" :class="{ 'p-invalid': errorMessage }" aria-describedby="text-error" />
                <label for="Email">Email</label>
        </span>
        <small class="p-error" id="text-error">{{ errorMessage || '&nbsp;' }}</small>
    </div>
</template>

<script setup>
import { useField } from 'vee-validate';
import InputText from 'primevue/inputtext'
const { value, errorMessage } = useField('email', validateMessage);

function validateMessage(value) {
    if (!value) {
        return 'Please enter an email address.';
    }

    return true;
}
</script>

<style lang="scss" scoped>
.input-field{
    padding-top: 1em;
    // padding-bottom: 1em;
}
</style>