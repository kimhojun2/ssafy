import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])
  const comments = ref([])
  const API_URL = 'http://127.0.0.1:8000'

  // DRF에 article 조회 요청을 보내는 action
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`
    })
      .then((res) => {
        console.log(res)
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }
  const getComments = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/comments/`
    })
      .then((res) => {
        console.log(res)
        comments.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }
  return { articles, API_URL, getArticles, getComments }
}, { persist: true })
