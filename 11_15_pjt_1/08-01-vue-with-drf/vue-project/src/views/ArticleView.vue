<template>
  <div>
    <ArticleList />
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { onMounted } from 'vue'
import ArticleList from '@/components/ArticleList.vue'
import { RouterLink } from 'vue-router'

const store = useCounterStore()

onMounted(() => {
  store.articles
})
</script>

<style>

</style>
