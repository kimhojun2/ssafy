<template>
    <div>
        <h1>상세 정보 페이지</h1>
        <div class="video-box">
            <h1> {{ videoTitle }} </h1>
            <iframe :src="videoUrl" frameborder="0" allowfullscreen class="video-card"></iframe>
            
            <p>{{ description }} </p>
            <p>{{ channelTitle }}</p>
            
            <button @click="saveVideo">{{ isVideoSaved ? '동영상 제거' : '동영상 저장' }}</button>

        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useRoute } from 'vue-router'


const route = useRoute()

const videoId = route.params.videoId
const videoTitle = ref('')
const videoUrl = ref('')
const channelTitle = ref('')
const description = ref('')
const sumnail = ref('')
const isVideoSaved = ref(false);
onMounted (() => {
    const apiKey = "AIzaSyB5LS4yS8W_xMsjVShF9yjtjscoPxhVqts"
    const apiURL = `https://www.googleapis.com/youtube/v3/videos?id=${videoId}&key=${apiKey}&part=snippet,contentDetails`

    axios.get(apiURL)
        .then(response => {
            const videoInfo = response.data.items[0]
            // console.log(videoInfo)
            videoTitle.value = videoInfo.snippet.title
            videoUrl.value = `https://www.youtube.com/embed/${videoId}`
            sumnail.value = videoInfo.snippet.thumbnails.default.url
            channelTitle.value = videoInfo.snippet.channelTitle
            description.value = videoInfo.snippet.description
        }) .catch (error => {
            console.error(error)
        })

})

const savedVideos = JSON.parse(localStorage.getItem('later')) || []
isVideoSaved.value = savedVideos.some(video => video.videoId === videoId)





const saveVideo = () => {
    const existingVideo = JSON.parse(localStorage.getItem('later')) || []
    console.log(existingVideo)
    const isDuplicate = existingVideo.length > 0 && existingVideo.find((item) => item.videoId === videoId)
    
    if (!isDuplicate) {
      alert('동영상을 저장합니다')
      existingVideo.push({videoId: videoId, title: videoTitle.value, url: sumnail.value})
      localStorage.setItem('later', JSON.stringify(existingVideo))
      
    } else {
      const updatedVideo = existingVideo.filter((item) => item.videoId !== videoId);
      
      localStorage.setItem('later', JSON.stringify(updatedVideo));
      alert('동영상을 목록에서 제거합니다')
    
    }
    isVideoSaved.value = !isVideoSaved.value

    // router.push('/cart')
}
</script>

<style scoped>
.video-box {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}
.video-card {
    display: flex;
    width: 800px;
    height: 400px;
    justify-content: center;
    align-items: center;
}

button {
  padding: 0.5rem 1rem;
  background-color: #4caf50;
  color: #fff;
  border: none;
  cursor: pointer;
  border-radius: 4px;
  transition: background-color 0.3s;

}
</style>