<template>
    <div>
        <h3>PostList component</h3>
        <hr>
    </div>
    <PostItem 
    v-for=" num in nums"/>
</template>

<script setup>
import PostItem from '@/components/post/PostItem.vue'
import { ref } from 'vue'
const nums = ref([1,2,3])
</script>

<style scoped>

</style>