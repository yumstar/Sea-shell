<template>
    <div class="create-message">
        <div class="message-composer">
            <form @submit="onSubmit" class="sign-in-form">
            <h2>Write down an affirmation.</h2>
            <MessageInputField />
            <Suspense>
            <ExistingTagInputField/>
            <template #fallback>
            <ProgressSpinner style="width: 50px; height: 50px" strokeWidth="8" fill="var(--surface-ground)"
    animationDuration=".5s" aria-label="Custom ProgressSpinner" />
            </template>
            </Suspense>
            <h4>New situation?</h4>
            <NewTagInputField />
            <Button type="submit" label="Save"/>
            </form>
        </div>
    </div>
</template>

<script setup>
import { useForm } from 'vee-validate';
import MessageInputField from './InputFields/MessageInputField.vue';
import ExistingTagInputField from './InputFields/ExistingTagInputField.vue';
import NewTagInputField from './InputFields/NewTagInputField.vue';
import ProgressSpinner from 'primevue/progressspinner';
import Button from 'primevue/button';
import { client } from '@/App.vue';
const { handleSubmit} = useForm();
const onSubmit = handleSubmit((values) =>{
    if (typeof values.newTags !== 'undefined'){
        let tagsToCheck = []
        values.newTags.forEach(tag => tagsToCheck.push({text: tag, color: "black"}))
        values.newTags = tagsToCheck
        console.log(values)
        for(var i = 0; i < tagsToCheck.length; i++){
            client.post("api/tag/", tagsToCheck[i])
        }
        
    }
} )
</script>

<style lang="scss" scoped>
.create-message {
    // border: var(--primary-color) solid 3px;
    display: flex;
    justify-content: center;
    padding: 2em;
    margin: auto;
    width: 50%;
    border-radius: var(--border-radius);
    box-shadow: -4px 3px 47px -2px rgba(232,228,228,0.75);
-webkit-box-shadow: -4px 3px 47px -2px rgba(232,228,228,0.75);
-moz-box-shadow: -4px 3px 47px -2px rgba(232,228,228,0.75);
:focus{
    box-shadow: var(--focus-ring);
}
}

.message-composer {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 2;
}
</style>