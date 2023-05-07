<template>
    <div class="sign-in">
        <form @submit="onSubmit" class="sign-in-form">
            <h1>Sign In</h1>
            <EmailInputField></EmailInputField>
            <PasswordInputField></PasswordInputField>
            <Button type="submit" label="Sign In" />
        </form>
    </div>
    <div class="register-redirect">
        <span>Don't have an account?</span>
        <router-link to="/register"> Sign Up!</router-link>
    </div>
</template>

<script setup>
import { useForm } from 'vee-validate';
import Button from 'primevue/button';
import EmailInputField from './InputFields/EmailInputField.vue';
import PasswordInputField from './InputFields/PasswordInputField.vue';
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
    // flex-direction: column;
    // min-width: fit-content;
    // height: 40em;
}

.sign-in-form{
        display: flex;
        flex-direction: column;
        gap: 2;
        // padding: 2em;
}

.register-redirect {
    margin: 2em;
    padding: 1em;
    border: 1px solid;
    margin: 2em auto;
    width: fit-content;
    display: flex;
    flex-direction: column;
    border-radius: var(--border-radius);
    // border-color: var(--primary-color);
    background-color: var(--primary-color);
    color: var(--primary-color-text);
    opacity: 1;
    // &:hover{
    //     animation: fadeIn 1s linear;
    //     animation-fill-mode: forwards;
    // }
    a {
        color: var(--secondary-color);
        &:hover {
            color: antiquewhite;
        }
    }

}

// @keyframes fadeIn {
//     0% {
//         opacity: 0.8;
//     }

//     1% {
//         opacity: 0.81;
//     }
//     50%{
//         opacity: 0.9;
//     }
//     100% {
//         opacity: 1;
//     }
// }

</style>