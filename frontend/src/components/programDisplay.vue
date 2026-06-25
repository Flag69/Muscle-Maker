<template>
    <div v-if="generatedProgram">

        <h2>Generated Program</h2>

        <div v-for="exercise in generatedProgram.exercises" :key="exercise.name">
            <h3>{{ exercise.name }}</h3>
            <p>{{ exercise.description }}</p>
        </div>
        
    </div>
</template>

<script setup>

defineProps({
  generatedProgram: {
    type: Object,
    required: true
  }
})

</script>

<style scoped> 
</style>