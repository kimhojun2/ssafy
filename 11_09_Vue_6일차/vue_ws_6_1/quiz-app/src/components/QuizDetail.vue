<template>
    <div v-for="quiz in quizzes">
        <div class="question">
            <h3>{{ quiz.pk }}번 문제. {{ quiz.question }}</h3>
            <div class="question__answer">
                <label for="ans">정답 입력</label>
                <input type="text" id="ans">
            </div>
        </div>
        
    </div>
</template>

<script setup>
const props = defineProps({
    quizzes: Array,
})
</script>

<style scoped>
.question {
    border: 1px solid rgb(202, 202, 202);
    width: 800px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 20px auto 20px auto;
    flex-direction: column;
    padding: 0 1rem;
    background-color: rgb(240, 238, 238);
    border-radius: 10px;
}
.question__answer {
    display: flex;
    flex-direction: column;
    width: 100%;
    padding: 1rem 0;
}

.question__answer > input {
    padding: 1rem;
    margin-top: 1rem;
    border-radius: .3rem;
    border: 1px solid rgba(128, 128, 128, 0.384);
    outline: none;
}
.question >h3 {
    text-align: left;
    width: 100%;
    margin: 50px;
}
</style>