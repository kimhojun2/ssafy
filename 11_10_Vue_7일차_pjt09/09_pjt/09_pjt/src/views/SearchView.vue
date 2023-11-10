<template>
    <div class="searchbox">
        <h1>검색 페이지</h1>
        <div>
            <input v-model="searchQuery" placeholder="동영상 검색어를 입력하세요" />
            <button @click="searchVideos">검색</button>
        </div>
        <div v-if="videos.length > 0">
            <h2 style="text-align: center; margin-top: 20px;">검색 결과</h2>
            <ul class="video-list">
                <div v-for="video in videos" :key="video.id.videoId" class="video-card">
                    <img :src="video.snippet.thumbnails.default.url" alt="">
                    <p @click="goToDetailView(video.id.videoId)">{{ video.snippet.title }}</p>
                    <p>{{ video.snippet.channelTitle }}</p>
                </div>
            </ul>
            
        </div>
        <div v-else>검색어를 입력하세요..</div>
    </div>                            
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const searchQuery = ref('')                                                                        
const videos = ref([])

const router = useRouter()

const searchVideos = () => {
    const apiKey = "AIzaSyB5LS4yS8W_xMsjVShF9yjtjscoPxhVqts"
    const apiURL = `https://www.googleapis.com/youtube/v3/search?key=${apiKey}&q=${searchQuery.value}&part=snippet&type=video&&maxResults=10`


axios.get(apiURL)
    .then((response) => {
        videos.value = response.data.items
    }) .catch(error => {
        console.error(error)
    })
}

const goToDetailView = (videoId) => {
  // 비디오 클릭 시 DetailView로 라우팅
  router.push({ name: 'detail', params: { videoId }});
};

</script>

<style scoped>
.video-list {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.video-card {
  border: 1px solid black;
  width: 200px;
  background-color: rgb(255, 221, 226);
  
}

.video-card img {
  width: 200px;
  height: 140px;
  object-fit: fill;
}

.video-card p{
  cursor: pointer;
  color: black
}

.searchbox {
    display: flex;
    justify-self: center;
    align-items: center;
    flex-direction: column;
}
</style>