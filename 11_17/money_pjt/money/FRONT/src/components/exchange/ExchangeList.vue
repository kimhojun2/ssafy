<template>
    <div class="moneychange">
      <h3>환율 계산기</h3>
      <select v-model="select_nm">
        <option v-for="(rate, index) in store.rates"
        :key="index"
        :value="rate">
        {{ rate.cur_nm }}
        </option>
      </select>
      <br>
      <div class="input_box">
        <input id="factor" v-model="factor" type="text" @input="validnum(factor)" class="money"/>
        <label for="factor">{{ lastElement }}</label>
        <br>
  
        <input id="result" v-model="result" type="text" @input="validnum(result)" class="money"/>
        <label for="result">원</label>
        <br>
      </div>
    </div>
  </template>
  
  <script setup>
  import { useCounterStore } from '@/stores/counter'
  import { def } from '@vue/shared';
  import { onMounted, computed, watch } from 'vue'
  import { ref } from 'vue';
  
  
  const store = useCounterStore()
  const default_nm = store.rates

  // const defaultValue = parseFloat(default_nm.replace(/,/g, ''))
  const select_nm = ref(default_nm)
  const factor = ref(1)
  const nm_unit = ref()
  const arr = ref(['달러'])
  const updateNM = () => {
    nm_unit.value = select_nm.value.cur_nm
    arr.value = nm_unit.value.split(' ')
    console.log(arr.value)
  }
  
  watch(select_nm, updateNM)
  
  const lastElement = computed(() => {
    return arr.value[arr.value.length - 1]
  })
  
  
  
  // const nm_length = NM(select_nm.value.cur_nm)
  
  // nm_unit.value = nm_length[nm_length.length-1]
  
  // console.log(NM(select_nm.value.cur_nm)[1])
  
  
  // 1번에 필요한거
  const MoneyUnit = ref(select_nm)
  const ChangeValue = (value) => {
    value = String(value)
    return parseFloat(value.replace(/,/g, ''))
  
  }
  const MoneyUnitChange = computed(()=>{
    return {
    changemoney: ChangeValue(MoneyUnit.value.deal_bas_r)
  }
  })
  
  
  const result = computed({
    get: () => (factor.value * MoneyUnitChange.value.changemoney),
    set: (value) => {
      factor.value = (value / MoneyUnitChange.value.changemoney)
    }
  })
  
  
  
  const validnum = (input) => {
    const testvalue = Number(input)
  
    if (isNaN(testvalue)) {
      alert('숫자만 입력하세요'),
      factor.value = 0
      console.log(typeof MoneyUnitChange)
    }
  }
  
  onMounted(() => {
    store.rates
  
  })
  
  
  
  </script>
  
  <style>
    /* 클릭됐을 때의 스타일을 지정하는 클래스를 정의합니다. */
    .money {
    border: none;
    /* 추가적으로 필요한 스타일을 지정할 수 있습니다. */
    text-align: right;
    font-size: 50px;
    width: 400px;
  
  } 
  .moneychange {
    text-align: center;
    align-items: center;
    margin-top: 200px;
  
  }
  </style>
  