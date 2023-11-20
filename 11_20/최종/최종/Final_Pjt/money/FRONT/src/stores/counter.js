import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const rates = ref([])
  const fins = ref([])
  const opts = ref([])
  const deps = ref([])
  const router = useRouter()
  const articles = ref([])
  const token = ref(null)
  const name = ref('')
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })


  const getFins = function () {
    axios({
      method: 'get',
      url: `${API_URL}/fin/deposit-products/`
    })
      .then((res) =>{
        fins.value = res.data

      })
      .catch((err) => {
        console.log(err)
      })
  }

  const logIn = function (payload) {
    const { username, password } = payload
    name.value = username
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((res) => {
        token.value = res.data.key
        router.push({ name: 'HomeView' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const signUp = function (payload) {
    const { username, password1, password2 } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2
      }
    })
      .then((res) => {
        console.log(res)
        const password = password1
        logIn({ username, password })
      })
      .catch((err) => {
        console.log(err)
      })
  }


  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
    })
      .then((res) => {
        token.value = null
        // articles.value = []
        router.push({ name: 'HomeView' })
      })
      .catch((err) => {
        console.log(err)
      })
  }


  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/articles/articles/`,
      // headers: {
      //   Authorization: `Token ${token.value}`
      // }
    })
      .then((res) =>{
        // console.log(res)
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getRates = function () {
    axios({
      method: 'get',
      url: `${API_URL}/exchange/rate/`
    })
      .then((res) => {
        rates.value = res.data
        console.log(rates.value)
      })
      .catch((err) => {
        console.log(err)
      })
  }

  
  const getdeps = function () {
    axios({
      method: 'get',
      url: `${API_URL}/fin/Generaldeposit-products`
    })
      .then((res) =>{
        console.log(res)
        deps.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }


  return {  name, articles, deps, fins, opts, API_URL, getRates, rates, getFins, getdeps, getArticles, signUp, logIn, token, isLogin, logOut }
},{persist:true})
