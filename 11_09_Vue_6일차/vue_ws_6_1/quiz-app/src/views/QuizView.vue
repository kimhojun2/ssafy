<template>
    <div>
        <QuizDetail :quizzes="quizzes"/>
    </div>
</template>

<script setup>
import QuizDetail from '../components/QuizDetail.vue';
import { ref } from 'vue'

const quizzes = ref([
    {pk:1,
    question:'They must often change who would be constant in happiness or wisdom.',
    answer:'1'},
    {pk:2,
    question:'Age is no guarantee of maturity.',
    answer:'2'},
    {pk:3,
    question:'You will face many defeats in life, but never let yourself be defeated.',
    answer:'3'},
    {pk:4,
    question:'The goal of life is living in agreement with nature. ',
    answer:'4'},
    {pk:5,
    question:'Only I can change me life, no one can do it for me. ',
    answer:'5'},])
</script>

<style scoped>

</style>