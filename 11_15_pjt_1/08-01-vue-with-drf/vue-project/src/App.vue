<template>
  <header>
    <nav>
      <RouterLink :to="{ name: 'HomeView'}">[HOME]</RouterLink> |
      <RouterLink :to="{ name: 'ArticleView'}">[환율 계산기]</RouterLink> |
      <RouterLink :to="{ name: 'CreateView'}">[지도]</RouterLink> 
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
</script>

<style scoped>
nav {
  text-align: center;
}

</style>
