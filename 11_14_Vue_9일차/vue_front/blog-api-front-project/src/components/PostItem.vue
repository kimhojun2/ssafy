<template>
    <div>
        <h5>{{ post.id }}</h5>
        <p>{{ post.title }}</p>
        <hr>
    </div>
</template>

<script setup>
defineProps({
    post: Object
})
</script>

<style scoped>

</style>