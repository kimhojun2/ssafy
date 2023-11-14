<template>
  <header>
    <nav>
      <RouterLink :to="{ name: 'Homeview'}">HOME</RouterLink>
      <RouterLink :to="{ name: 'Postview'}">POST</RouterLink>
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
</script>

<style scoped>

</style>