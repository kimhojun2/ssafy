<template>
    <div :style="containerStyle">
        <h1>가주 정보 페이지에 오신 것을 환영합니다</h1>
        <p>여러분이 좋아하는 가수와 아티스트에 대한 정보를 탐색해보세요.</p>
        <img src="../assets/microphone.jpg" alt="" :style="{ width: imgSize.width }">
    </div>
</template>

<script setup>
import { ref } from 'vue'
const imgSize = ref({ width: '200px'})
const containerStyle = {
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center',
    }
</script>

<style scoped>

</style>