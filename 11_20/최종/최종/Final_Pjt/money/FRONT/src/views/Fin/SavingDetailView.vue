<template>
    <div>
      <div v-if="isLoading">Loading...</div>
      <div v-else>
        <!-- Your actual content goes here -->
        <div>
          <h1>상품 이름 : {{ saving.fin_prdt_nm }}</h1>
          <button>가입하기</button>
        </div>  
        <h2>은행 이름 : {{ saving.kor_co_nm }}</h2>
          <div v-for="option in saving.options">
              <div>
                  단/복 : {{ option.intr_rate_type_nm }}
                  금리 : {{ option.intr_rate }}
                  최고 금리 :{{ option.intr_rate2 }}
                  예금 기간 :{{ option.save_trm }}
              </div>
          </div>
          <button @click="goBack">목록으로 돌아가기</button>
      </div>
    </div>
  </template>
  
  <script setup>  
  import axios from 'axios'
  import { ref, computed, onMounted } from 'vue'
  import { useCounterStore } from '@/stores/counter'
  import { RouterLink } from 'vue-router'
  import { useRoute, useRouter } from 'vue-router'
  
  const store = useCounterStore()
  const route = useRoute()
  const router = useRouter()
  const saving = ref(null)
  const isLoading = ref(true);
  
  const goBack = () => {
      router.go(-1)
      console.log('눌렸음')
  }
  
  
  onMounted(() => {
      axios({
          method : 'get',
          url: `${store.API_URL}/fin/saving-product/${route.params.id}/`,
      }) .then((res) => {
          saving.value = res.data
          console.log(res.data)
      }) .catch((err)=> console.log(err))
      .finally(() => {
            isLoading.value = false; // Set isLoading to false once the request is complete
          });
  })
  
  
  
  </script>
  
  <style scoped>
  
  </style>