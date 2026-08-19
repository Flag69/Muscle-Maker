<template>
    <div v-if="generatedProgram">

        <h2>Generated Program</h2>

        <div v-for="exercise in generatedProgram.exercises" :key="exercise.name" class="exercise-card">
            <h3>{{ exercise.Name }}</h3>
            <p>{{ exercise.Description }}</p>
            <p>{{ exercise.Sets }} x {{ exercise.Reps }} {{ exercise.RepsType === "time" ? "s" : "reps" }} {{ exercise.Sets > 1 ? ", " + exercise.Rest + "s rest" : ""}}</p>
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

.exercise-card {
  border: 1px solid #ccc;
  padding: 10px;
  margin-bottom: 10px;
  border-radius: 5px;
}

.exercise-card h3 {
  margin: 0;
  font-size: 1.2em;
}

.exercise-card p {
  margin: 0px 0;
}

</style>