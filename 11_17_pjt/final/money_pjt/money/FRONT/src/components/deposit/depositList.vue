<template>
    <div>
      <h1>검색하기</h1>
      
      <select v-model="testData" :onChange="test">
        <option value="">전체 은행</option>
        <option v-for="bank in uniqueBanks" :key="bank" :value="bank">{{ bank }}</option>
      </select>
      <button @click="searchDeposits">검색</button>

      <ul v-if="currentState">
          <depositItem 
          :selectedBank="selectedBank"
          :filteredDeposits="filteredDeposits" />
      </ul>
    </div>
  </template>
  
<script setup>
import { useCounterStore } from '@/stores/counter';
import { computed, ref, watch, onMounted } from 'vue';
import depositItem from './depositItem.vue';

const store = useCounterStore();

const testData = ref("")
const selectedBank = ref(null);
const currentState = ref(true)

const test = () => {
    selectedBank.value = testData.value
    if (currentState.value) {
        currentState.value = !currentState.value
    }
}

// 전역으로 선언된 computed 속성
const filteredDeposits = computed(() => {
    if (!selectedBank.value) {
        console.log(1)
      return store.deposits;
    }
    console.log(2)
  // 선택된 은행에 해당하는 예금 항목들만 필터링
  return store.deposits.filter(deposit => deposit.kor_co_nm === selectedBank.value);
});



const uniqueBanks = computed(() => {
// 중복을 제거한 은행 목록을 가져옴
console.log(uniqueBanks)
return [...new Set(store.deposits.map(deposit => deposit.kor_co_nm))];
});

const searchDeposits = () => {
    currentState.value = !currentState.value
// searchDeposits 함수가 호출될 때만 filteredDeposits를 다시 계산

};


</script>
  
<style scoped>

</style>