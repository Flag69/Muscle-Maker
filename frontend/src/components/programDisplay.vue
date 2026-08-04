<template>
    <div v-if="generatedProgram">

        <h2>Generated Program</h2>

        <div v-for="exercise in generatedProgram.exercises" :key="exercise.name">
            <h3>{{ exercise.Name }}</h3>
            <p>{{ exercise.Description }}</p>
            <p>{{ exercise.Sets }} x {{ exercise.Reps }} reps</p>
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