<template>
    <div class="sign-in">
        <form @submit="onSubmit" class="sign-in-form">
            <h1>Sign In</h1>
            <EmailInputField></EmailInputField>
            <PasswordInputField></PasswordInputField>
            <Button type="submit" label="Submit" />
        </form>
    </div>
</template>

<script setup>
import { useForm } from 'vee-validate';
import Button from 'primevue/button';
import EmailInputField from './EmailInputField.vue';
import PasswordInputField from './PasswordInputField.vue';
import {client} from "../App.vue"

const { handleSubmit, resetForm } = useForm();
const onSubmit = handleSubmit((values) =>{
    client.post("api/centerUser/signin", values)
    .then((res) => {
        console.log(res)
    })
    resetForm()
} )
</script>

<style lang="scss" scoped>
.sign-in{
    display: flex;
    justify-content: center;
    // height: 40em;
}

.sign-in-form{
        display: flex;
        flex-direction: column;
        gap: 2;
        // padding: 2em;
}


</style>