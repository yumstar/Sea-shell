<template>
    <div class="input-field">
        <span class="p-float-label">
                <InputText id="name" v-model="value" type="text" :class="{ 'p-invalid': errorMessage }" aria-describedby="text-error" />
                <label for="Name">Name</label>
        </span>
        <small class="p-error" id="text-error">{{ errorMessage || '&nbsp;' }}</small>
    </div>
</template>

<script setup>
import { useField } from 'vee-validate';
import InputText from 'primevue/inputtext'
const { value, errorMessage } = useField('name', validateMessage);

function validateMessage(value) {
    if (!value) {
        return 'Please enter your name.';
    }

    return true;
}
</script>

<style lang="scss" scoped>
.input-field{
    padding-top: 1em;
}
</style>