<template>
                <div class="input-field">
                <span class="p-float-label">
                <Password id="password" v-model="value" type="text" :class="{ 'p-invalid': errorMessage }" aria-describedby="text-error" :feedback="false"/>
                <label for="password">Password</label>
            </span>
            <small class="p-error" id="text-error">{{ errorMessage || '&nbsp;' }}</small>
        </div>
</template>
<script setup>
import { useField } from 'vee-validate';
import Password from 'primevue/password'
const { value, errorMessage } = useField('password', validateMessage);

function validateMessage(value) {
    if (!value) {
        return 'Password is required.';
    }

    return true;
}
</script>

<style lang="scss" scoped>
.input-field{
    padding-top: 1em;
}
</style>