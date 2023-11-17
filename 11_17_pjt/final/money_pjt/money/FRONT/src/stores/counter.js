import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const deposits = ref([])
  const rates = ref([])
  const getDeposits = function () {
    axios({
      method: 'get',
      url: `${API_URL}/fin/deposit-products`
    }) .then(res => {
      deposits.value = res.data
    }) .catch(err => console.log(err))
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


  return { deposits, getDeposits, getRates, rates }
})
