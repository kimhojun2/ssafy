<template>
    <div>
        <h1>POST LIST</h1>
        <PostList />
    </div>
</template>

<script setup>
import PostList from '@/components/PostList.vue'
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'


const store = useCounterStore()

onMounted(() => {
    store.posts
    console.log(store.posts)
})

</script>

<style lang="scss" scoped>

</style>