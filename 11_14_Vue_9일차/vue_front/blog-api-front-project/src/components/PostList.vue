<template>
    <div>
        <h1>리스트 컴포넌트</h1>
        <PostItem
        v-for="post in store.posts"
        :key="post.id"
        :post="post"
        />
    </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import PostItem from './PostItem.vue'

const store = useCounterStore()
</script>

<style scoped>

</style>