<template>
    <div class="container">
        <h1 class="singer-name">가수 이름</h1>
        <img src="@/assets/singer.jpg" alt="singer" class="singer-img">
        <p>가수 소게글</p>
    </div>
</template>

<script setup>

</script>

<style scoped>
.container {
    border: 1px solid black;
    width: 80%;
    height: 500px;
    display: flex;
    justify-content: center; 
    align-items: center; 
    flex-direction: column; /* 수직 방향으로 아이템들을 정렬 */
    text-align: center; /* 가로 가운데 정렬 */
    margin: 0 auto;
}
.singer-img {
    width: 200px;
    border-radius: 50%;
}
.singer-name {
    margin-bottom: 100px;

}
</style>