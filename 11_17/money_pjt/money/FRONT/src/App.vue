<template>
  <header>
    <nav>
      <RouterLink :to="{ name: 'HomeView' }">HOME</RouterLink>  |
      <RouterLink :to="{ name: 'FinView' }">Fin</RouterLink>  |
      <RouterLink :to="{ name: 'MapView' }">Map</RouterLink>  |
      <RouterLink :to="{ name: 'ExchangeRateView' }">ExchangeRate</RouterLink>
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<style scoped>

</style>