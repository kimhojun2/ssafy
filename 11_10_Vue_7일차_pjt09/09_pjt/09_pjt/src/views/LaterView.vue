<template>
    <div>
        <h1>장바구니</h1>
        <div v-if="laterItems">
            <h2>저장한 동영상</h2>
            <ul class="video-list">
                <div v-for="video in laterItems" :key="video.videoId">
                    <div class="later-card">
                      <img :src="video.url" alt="">
                      <p @click="goToDetailView(video.videoId)">{{ video.title }}</p>
                      
                    </div>
                </div>
            </ul>
        </div>
        <div v-else>
            <strong>장바구에 담긴 상품이 없습니다.</strong>
        </div>
    </div>
  </template>
  
  <script setup>
  import { useRouter } from 'vue-router'
  import { ref, onMounted } from 'vue'
  
  const router = useRouter()

  const laterItems = ref([])

  laterItems.value = JSON.parse(localStorage.getItem('later'))

  const goToDetailView = (videoId) => {
  // 비디오 클릭 시 DetailView로 라우팅
  router.push({ name: 'detail', params: { videoId } });

};

  
  </script>
  
  


  <style scoped>
  .later-card {
    border: 1px solid black;
    widows: 300px;
    text-align: center;
  }
  .later-card img {
    width: 300px;
    height: 180px;
    object-fit: fill;
  }

  .later-card p{
  cursor: pointer;
  color: black
}

  .video-list {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}
  </style>