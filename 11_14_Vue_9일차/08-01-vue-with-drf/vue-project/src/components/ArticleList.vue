<template>
  <div>
    <h3>Article List</h3>
    <p v-for="article in store.articles">
      <div v-if="article.cur_unit.length > 3">
        1{{article.cur_nm}}는  {{ article.deal_bas_r/100 }}
      </div>
      <div v-else style="color: red;">
        1{{article.cur_nm}}는 : {{ article.deal_bas_r }}
      </div>
      
      
    </p>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import ArticleListItem from '@/components/ArticleListItem.vue'


const store = useCounterStore()
</script>
