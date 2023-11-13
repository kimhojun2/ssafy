<template>
    <div>
        <TodoListitem
            v-for="todo in store.todos"
            :key="todo.id"
            :todo="todo"
        />
    </div>
</template>

<script setup>
import TodoListitem from '@/components/TodoListitem.vue'
import { useCounterStore  } from '@/stores/counter'

const store = useCounterStore()
</script>

<style scoped>

</style>