<template>
    <CContainer class="experience-reporter">
        <ExperienceChoiceCard v-for="(experience, index) in experiences" :name="experience.word" :value="experience.rank" :icon="experience.icon" class="experience-choice" :class="{selected: index == selectedIndex.selected}" :selected="index == selectedIndex.selected" :key="experience.word" @click="setSelected(index)"></ExperienceChoiceCard>
    </CContainer>
</template>

<script setup>
import { CContainer } from '@coreui/vue';
import { reactive, ref } from 'vue';
import ExperienceChoiceCard from './ExperienceChoiceCard.vue';
const experiences = ref([
    {
    word: "Great",
    rank: 5,
    icon: 'cilMoodVeryGood'
    },
    {
    word: "Good",
    rank: 4,
    icon: 'cilMoodGood'
    },
    {
    word: "Okay",
    rank: 3,
    icon: 'cilMeh'
    },
    {
    word: "Subpar",
    rank: 2,
    icon: 'cilSad'
    },
    {
    word: "Awful",
    rank: 1,
    icon: 'cilMoodBad'
    },
])

const selectedIndex = reactive({
    selected: -1
})
const setSelected = (index) =>{
    selectedIndex.selected = index
}


</script>

<style lang="scss" scoped>
.experience-reporter{

    margin: auto;
    max-width: 90%;
    min-height: 40%;
    height: 40%;
    display: flex;
    box-shadow: -4px 3px 47px -2px rgba(232,228,228,0.75);
-webkit-box-shadow: -4px 3px 47px -2px rgba(232,228,228,0.75);
-moz-box-shadow: -4px 3px 47px -2px rgba(232,228,228,0.75);
}

.selected{
        border: 2px solid rgba(80,149,255,0.27);
    }
</style>