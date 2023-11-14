import { createRouter, createWebHistory } from 'vue-router'
import Postview from '../views/PostView.vue'
import Homeview from '../views/Homeview.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
      {
          path: '/',
          name: 'Homeview', 
          component: Homeview
        },
        {
          path: '/postlist',
          name: 'Postview',
          component: Postview
        },
  ]
})

export default router
