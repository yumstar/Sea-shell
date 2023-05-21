<template>
    <div class="create-message">
        <div class="message-composer">
            <h2>Write down an affirmation.</h2>
            <MessageInputField />
            <h4>Mark it for when you need it.</h4>
            <ExistingTagInputField/>
            <h4>New situation?</h4>
            <NewTagInputField />
        </div>
    </div>
</template>

<script setup>
import MessageInputField from './InputFields/MessageInputField.vue';
import ExistingTagInputField from './InputFields/ExistingTagInputField.vue';
import NewTagInputField from './InputFields/NewTagInputField.vue';
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