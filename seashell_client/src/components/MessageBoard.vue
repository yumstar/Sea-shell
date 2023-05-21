<template>
    <div>
        <div class="message-board">
            <MessageBlock v-for="item in state.messages" :key="item.id" :body="item.body" :tags="item.tags"/>
        </div>
    </div>
</template>

<script setup>
import { client } from '@/App.vue';
import { reactive} from 'vue';
import MessageBlock from './Blocks/MessageBlock.vue';
var state = reactive({
    messages: []
})
const res = await client.get("/api/message/")
state.messages = res.data
</script>

<style lang="scss" scoped>
.message-board {
    display: flex;
    margin: 2em auto;
    width: 80%;
    min-height: 12em;
    border-radius: var(--border-radius);
    box-shadow: -4px 3px 47px -2px rgba(232,228,228,0.75);
-webkit-box-shadow: -4px 3px 47px -2px rgba(232,228,228,0.75);
-moz-box-shadow: -4px 3px 47px -2px rgba(232,228,228,0.75);
}
</style>