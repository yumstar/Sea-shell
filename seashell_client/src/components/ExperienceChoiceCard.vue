<template>
        <CContainer ref="container">
            <p>{{props.name}}</p>
            <CIcon :icon="props.icon" size="xxl"/>
            <CButton v-if="props.selected" class="check-in-button" :class="{selectedButton: props.selected}">Check in</CButton>
        </CContainer>
</template>

<script setup>
import CIcon from '@coreui/icons-vue';
import { CButton, CContainer } from '@coreui/vue';
import { defineProps} from 'vue';
const props = defineProps({
    name: String,
    value: Number,
    icon: String,
    selected: Boolean
})
</script>

<style lang="scss" scoped>
.experience-choice{
    border: 1px solid rgba(204,195,195,0.21);
    // border: 4px solid rgba(80,149,255,0.27);
    height: 15em;
    max-height: 20vh;
    margin: 1em;
    border-radius: 0.7em;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    box-shadow: -4px 3px 47px -2px rgba(232,228,228,0.75);
-webkit-box-shadow: -4px 3px 47px -2px rgba(232,228,228,0.75);
-moz-box-shadow: -4px 3px 47px -2px rgba(232,228,228,0.75);
}
.check-in-button {
    margin: 1em;
    border: 1px solid black;
    // opacity: 0;
    // display: block;
}

.selectedButton{
    -webkit-animation: fadeIn 1s linear;
    -moz-animation: fadeIn 1s linear;
    -o-animation: fadeIn 1s linear;
    animation: fadeIn 1s linear;
    }

@-webkit-keyframes fadeIn {
    0% {
        display: none;
        opacity: 0;
    }

    1% {
        display: block;
        opacity: 0;
    }

    50%{
        display: block;
        opacity: 0.5;
    }
    100% {
        display: block;
        opacity: 1;
    }
}

@-moz-keyframes fadeIn {
    0% {
        display: none;
        opacity: 0;
    }

    1% {
        display: block;
        opacity: 0;
    }
    50%{
        display: block;
        opacity: 0.5;
    }
    100% {
        display: block;
        opacity: 1;
    }
}

@-o-keyframes fadeIn {
    0% {
        display: none;
        opacity: 0;
    }

    1% {
        display: block;
        opacity: 0;
    }
    50%{
        display: block;
        opacity: 0.5;
    }
    100% {
        display: block;
        opacity: 1;
    }
}

@keyframes fadeIn {
    0% {
        display: none;
        opacity: 0;
    }

    1% {
        display: block;
        opacity: 0;
    }
    50%{
        display: block;
        opacity: 0.5;
    }
    100% {
        display: block;
        opacity: 1;
    }
}
.selected{
        border: 2px solid rgba(80,149,255,0.27);
    }
</style>