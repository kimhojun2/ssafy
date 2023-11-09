<template>
  <div class="container">
    <div class="big-box">
      <div class="orange-box">
        <h1>Quiz 퀴즈</h1>
      </div>
      <p>여기는 퀴즈의 나라!놀라운 퀴즈들이 기다리고 있어요. 지금 바로 도전해보세요!</p>
    </div>
    <div class="small-box">
      <nav>
      <RouterLink :to="{ name: 'home' }">Home | </RouterLink>
      <RouterLink :to="{ name: 'quiz' }">Quiz |</RouterLink>
      </nav>
    </div>
  </div>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { ref } from 'vue'




</script>

<style scoped>
.container {
  background-color: rgb(240, 238, 238);
  width: 700px;
  height: 300px;

  display: flex;
  justify-content: space-around;
  align-items: center;
  margin: 0 auto;
  flex-direction: column;
  
}

.big-box {
  text-align: center;
  background-color: white;
  width: 600px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-direction: column;
  border-radius: 10px;
}

.big-box >p {
  padding: 2.5rem 0;
}


.small-box {
  text-align: center;
  background-color: black;
  color: white;
  
  width: 600px;
}

.small-box >nav {
  margin: .5rem 0;
}

nav a {
  text-decoration: none;
  color: white;
}
.orange-box {
  color: white;
  background-color: orange;
  border-radius: 10px 10px 0 0;
  width: 100%;
  /* height: 50px; */
}

.orange-box >h1 {
  margin: 0.5rem 0;
}


</style>