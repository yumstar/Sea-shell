<template>
    <div class="register">
        <form @submit="onSubmit" class="register-form">
            <h1>Register</h1>
            <EmailInputField></EmailInputField>
            <PasswordInputField></PasswordInputField>
            <NameInputField></NameInputField>
            <Button type="submit" label="Register" />
        </form>
    </div>
    <div class="sign-in-redirect">
        <span>Already have an account?</span>
        <router-link to="/sign-in"> Sign In!</router-link>
    </div>
</template>

<script setup>
import { useForm } from 'vee-validate';
import Button from 'primevue/button';
import EmailInputField from './InputFields/EmailInputField.vue';
import PasswordInputField from './InputFields/PasswordInputField.vue';
import NameInputField from './InputFields/NameInputField.vue'
import {client} from "../App.vue"
import router from '@/router';

const { handleSubmit, resetForm } = useForm();
const onSubmit = handleSubmit((values) =>{
    client.post("api/centerUser/register", values)
    .then((res) => {
        if(res.status >= 200 && res.status < 300){
            router.push("/sign-in")
        }
    })
    resetForm()
} )

</script>

<style lang="scss" scoped>
.register{
    display: flex;
    justify-content: center;
}

.register-form{
        display: flex;
        flex-direction: column;
        gap: 2;
}

.sign-in-redirect {
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