import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import FinView from '@/views/FinView.vue'
import MapView from '@/views/MapView.vue'
import ExchangeRateView from '@/views/ExchangeRateView.vue'
import PostView from '@/views/PostView.vue'
import Newjeans from '@/views/Newjeans.vue'
import MainPageView from '@/views/MainPageView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/FinView/',
      name: 'FinView',
      component: FinView
    },
    {
      path: '/MapView/',
      name: 'MapView',
      component: MapView
    },
    {
      path: '/ExchangeRateView',
      name: 'ExchangeRateView',
      component: ExchangeRateView
    },
    {
      path: '/PostView/',
      name: 'PostView',
      component: PostView
    },
    {
      path: '/Newjeans/',
      name: 'Newjeans',
      component: Newjeans
    },
    {
      path: '/HomeView/',
      name: 'HomeView',
      component: HomeView
    },
    {
      path: '/',
      name: 'MainPageView',
      component: MainPageView
    },
    
  ]
})

export default router
