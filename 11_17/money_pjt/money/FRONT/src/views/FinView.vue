<template>
    <div>
        <h1>Fin</h1>
        <depositList />
    </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { onMounted } from 'vue'
import depositList from '@/components/deposit/depositList.vue'
import { RouterLink } from 'vue-router'

const store = useCounterStore()

onMounted(()=>{
    store.getDeposits()
})

</script>

<style scoped>

</style>