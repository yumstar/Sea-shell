<template>
    <div class="input-field">
        <span class="p-float-label">
            <MultiSelect id="existing-tags" v-model="value" :options="state.tags" optionLabel="name"  display="chip" placeholder="Select Cities" class="input-field-multi-select" filter/>
                <label for="existing-tags">Existing Tags</label>
        </span>
        <small class="p-error" id="text-error">{{ errorMessage || '&nbsp;' }}</small>
    </div>
</template>

<script setup>
import { useField } from 'vee-validate';
import { client } from '@/App.vue';
import { reactive} from 'vue';
import MultiSelect from 'primevue/multiselect'
const { value, errorMessage } = useField('existing-tags', validateTag);

var state = reactive({
    tags: []
})
const res = await client.get("/api/tag/")
const tagList = res.data.map((tag) => {return {name: tag.text, code: tag.id}})
state.tags = tagList

function validateTag() {
    // if (!value) {
    //     return 'Please mark the tags for your message.';
    // }

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