<template>
    <div class="img-box">
        <h3 style="width: 100%;">퀴즈 앱 사용 방법</h3>
        <h1>1. 퀴즈 목록 확인하기</h1>
        <p>퀴즈 목록 페이지에서 다양한 퀴즈를 확인하세요.</p>
        <div class="line-box">
        <img src="@/assets/quizList.png" alt="answer">
        </div>
        <h1>2. 퀴즈 생성하기</h1>
        <p>퀴즈는 직접 생성 할 수도 있어요.</p>
        <div class="line-box">
        <img src="@/assets/quizCreate.png" alt="answer">
        </div>
        <h1>3. 정답 페이지</h1>
        <p>작성한 답안이 정답인지 확인하세요.</p>
        <div class="line-box">
        <img src="@/assets/quizAnswer.png" alt="answer">
        </div>
    </div>
</template>

<script setup>

</script>

<style scoped>
.img-box {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    width: 900px;
    margin: 10px auto 0px auto;
    
}

.line-box {
    border: 1px solid rgb(202, 202, 202);
    width: 900px;
    margin: 30px;
}

.img-box >h1 {
    /* text-align: left; */
    width: 100%;
}

.img-box >p {
    /* text-align: left; */
    width: 100%;
}

img {
    width: 100%;
}
</style>