import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import FinView from '@/views/FinView.vue'
import MapView from '@/views/MapView.vue'
import ExchangeRateView from '@/views/ExchangeRateView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'HomeView',
      component: HomeView
    },
    {
      path: '/FinView/',
      name: 'FinView',
      component: FinView
    },
    {
      path: '/b',
      name: 'MapView',
      component: MapView
    },
    {
      path: '/c',
      name: 'ExchangeRateView',
      component: ExchangeRateView
    },
  ]
})

export default router
