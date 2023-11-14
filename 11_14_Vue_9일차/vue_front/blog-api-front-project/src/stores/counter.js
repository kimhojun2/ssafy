import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
    const posts = ref([
        { id: 1, title: 1 },
        { id: 2, title: 2 }
    ])
  return { posts }
})
