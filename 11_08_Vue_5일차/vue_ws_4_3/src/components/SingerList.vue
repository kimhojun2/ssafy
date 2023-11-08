<template>
    <div class="container">
        <h1>가수 목록</h1>
        <SingerDetail />
    </div>
</template>

<script setup>
import SingerDetail from './singers/SingerDetail.vue';

</script>

<style scoped>
.container {

    display: flex;
    justify-content: center; 
    align-items: center; 
    flex-direction: column; /* 수직 방향으로 아이템들을 정렬 */
    text-align: center; /* 가로 가운데 정렬 */
    margin-top: 100px;
}
</style>