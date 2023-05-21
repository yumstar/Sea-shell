<template>
    <div class="input-field">
        <span class="p-float-label">
            <MultiSelect v-model="value" :options="cities" optionLabel="name"  display="chip" placeholder="Select Cities" class="input-field-multi-select" filter/>
                <label for="message">Existing Tags</label>
        </span>
        <small class="p-error" id="text-error">{{ errorMessage || '&nbsp;' }}</small>
    </div>
</template>

<script setup>
import { useField } from 'vee-validate';
// import Textarea from 'primevue/textarea'
import MultiSelect from 'primevue/multiselect'
const { value, errorMessage } = useField('message', validateTag);
const cities = [
    { name: 'New York', code: 'NY' },
    { name: 'Rome', code: 'RM' },
    { name: 'London', code: 'LDN' },
    { name: 'Istanbul', code: 'IST' },
    { name: 'Paris', code: 'PRS' }
];
function validateTag(value) {
    if (!value) {
        return 'Please mark the tags for your message.';
    }

    return true;
}
</script>

<style lang="scss" scoped>
.input-field{
    padding-top: 1em;
}
.input-field-multi-select{
    max-width: 25em;
    width: 25em;
}
</style>