<template>
  <div>
    <h1>Detail</h1>
    <p>제목 : {{ article.title }}</p>
    <p>내용 : {{ article.content }}</p>
    <p>작성일 : {{ article.created_at }}</p>
    <p>수정일 : {{ article.updated_at }}</p>
    {{ comment[0] }}
    {{ article }}
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute } from 'vue-router'

const store = useCounterStore()
const route = useRoute()
const article = ref({})
const comment = ref({})

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}`
  })
  .then((res) => {
    console.log(res)
    article.value = res.data
  })
  .catch((err) => {
    console.log(err)
  })
  

  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/comments/`
  })
  .then((res) => {
    console.log(res)
    comment.value = res.data
  })
  .catch((err) => {
    console.log(err)
  })
})


</script>

<style>

</style>
