<template>
    <div v-if="generatedProgram">

        <h3>Generated Program
          <span>
            <button @click="showDescription = !showDescription">
              {{ showDescription ? "Hide descriptions" : "Show descriptions" }}
            </button>
          </span>
        </h3>

        <div v-for="exercise in generatedProgram.exercises" :key="exercise.name" class="exercise-card">
            <h4>{{ exercise.Name }}</h4>
            <p v-if="showDescription">{{ exercise.Description }}</p>
            <p>{{ exercise.Sets }} x {{ exercise.RepsType === "time" ? formatRepsType(exercise.RepsType, exercise.Reps) : exercise.Reps + " reps" }} {{ exercise.Sets > 1 ? " / " + formatRepsType("time", exercise.Rest) + " rest" : ""}}</p>
        </div>
        
    </div>
</template>

<script setup>

import { ref } from "vue";

const showDescription = ref(false);


defineProps({
  generatedProgram: {
    type: Object,
    required: true
  }
})

function formatRepsType(repsType, reps) {
  if (repsType === "time") {
    let minutes = Math.floor(reps / 60);
    let seconds = reps % 60;

  if (minutes === 0) {
    return `${seconds}s`;
  } else if (seconds === 0) {
    return `${minutes} min`;
  }

  return `${minutes}min ${seconds}s`;
  }
}

</script>

<style scoped> 

.exercise-card {
  border: 1px solid #ccc;
  padding: 5px;
  margin-bottom: 5px;
  border-radius: 5px;
}

.exercise-card h4 {
  margin: 0;
  font-size: 0.8em;
}

.exercise-card p {
  margin: 0;
  font-size: 0.7em;
}

.exercise-card p {
  margin: 0px 0;
}

</style>