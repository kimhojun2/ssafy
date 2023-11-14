<template>
  <div>
    <h1>Article Page</h1>
    <RouterLink :to="{ name: 'CreateView' }">
      [CREATE]
    </RouterLink>
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
  store.getArticles(),
  store.getComments(),
  store.articles
})
</script>

<style>

</style>
