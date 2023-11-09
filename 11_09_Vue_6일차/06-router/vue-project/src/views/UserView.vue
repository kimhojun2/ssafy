<template>
    <div>
        <h1>UserView</h1>
        <h2>{{ $route.params.id }}번 유저의 페이지입니다.</h2>
        <h2>{{ userId }}</h2>
        <button @click="goHome">호므로!</button>
        <button @click="goAnotherUser">100번 유저 페이지로!</button>
    </div>
</template>

<script setup>
import { useRoute, useRouter, onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router'
import { ref } from 'vue'

const route = useRoute()
const userId = ref(route.params.id)
const router = useRouter()

const goHome = function() {
    router.push({ name: 'home' })
}

// In-component Guard
onBeforeRouteLeave((to, from) => {
    const answer = window.confirm('정말 떠나실 건가요?')
    if (answer === false) {
        return false
    }
})

// onBeforeTouteUpdate
const goAnotherUser = function () {
    router.push({ name: 'user', params: {id: 100} })
}

onBeforeRouteUpdate((to, from) => {
    userId.value = to.params.id
})

</script>

<style scoped>

</style>