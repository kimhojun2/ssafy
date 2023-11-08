<template>
    <div class="header">
        <h1>랜덤한 강아지</h1>
        <button @click="getRandomDogData">새로운 강아지 가져오기</button>
    </div>
    <div v-if="dogIsEmpty" class="dog-container">
        <div v-for="dog in dogs" class="dog-box">
            <img :src="dog.url" alt="" class="dog-box img">
            <div v-if="dog.detail" class="dog-info">
                <p><strong>이름 :</strong> {{ dog.detail.name }}</p>
            </div>
            <div v-else class="dog-info">
                이름 없음
            </div>
        </div>
    </div>
    <div v-else>
        아직 데이터를 받오지 않았다
    </div>
</template>

<script setup>
import { computed } from 'vue'
const emit = defineEmits(['getDogData'])

const dogIsEmpty = computed(() => {
    return props.dogs.length > 0 ? true : false
})

const getRandomDogData = () => {
    emit('getDogData')
}

const props = defineProps({
    dogs: Array,
})

</script>

<style scoped>
.header {
    display: flex;
    justify-content: space-between;
    margin-bottom: 20px;
    
}

button {
    padding: 10px 20px;
    background-color: #3498db;
    background-image: linear-gradient(to left, #9ab2ff, #fecff2); /* 그라데이션 적용 */
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
    transition: background-color 0.3s;
}
button:hover {
    background-color: #2980b9;
}

.dog-container {
    border: 40px solid black;
    border-radius: 20px;
    background-color: aqua;

}

.dog-box {
    border: 5px solid black;
    border-radius: 10px;
    margin: 10px;
    display: flex;
    background-image: linear-gradient(to left, #ffe49a, #cff1fe);
}

.dog-box img {
    width: 200px;
    height: 200px;
    object-fit: fill;
    border-radius: 10px;
}

.dog-info {
    font-size: 50px;
    margin-top: 20px;
    margin-left: 30px;
    color: red;
}
</style>