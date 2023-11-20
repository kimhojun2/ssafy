<template>
    <div v-if="isLoading">Loading...</div>
    <div v-else>
        {{ info }}
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
const info = ref(null)
const isLoading = ref(true);


onMounted(() => {
    axios({
        method : 'get',
        url: `${store.API_URL}/accounts/accounts/${route.params.username}/`,
    }) .then((res) => {
        info.value = res.data
        // console.log(res.data)
    }) .catch((err)=> console.log(err))
    .finally(() => {
          isLoading.value = false; // Set isLoading to false once the request is complete
        });
})

</script>

<style scoped>

</style>