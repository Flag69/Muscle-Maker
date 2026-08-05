<template>
  <h1>Muscle Maker</h1>

  <!-- Div to place filters -->
  <h4>Filters
    <span>
        <button @click="showFilters = !showFilters">
          {{ showFilters ? "▼" : "▶" }}
        </button>
    </span>
    <div v-if="showFilters">
      <filtersDisplay v-model="filters" />
    </div>
  </h4>

  <!-- Div to place generation buttons -->
  <div>
    <generateButton @generateProgram="handleGenerateProgram" />
  </div>

  <!-- Div to display generated program -->
  <div v-if="generatedProgram">
    <programDisplay :generatedProgram="generatedProgram" />
  </div> 

</template>

<script setup>
import { ref } from "vue"
import { generate_program } from "@/services/api"
import generateButton from "@/components/generateButton.vue"
import programDisplay from "@/components/programDisplay.vue"
import filtersDisplay from "@/components/filtersDisplay.vue"

const generatedProgram = ref(null)

const showFilters = ref(false)

const filters = ref({
  programDuration: 60,
  programDifficulty: 1,
  programGoal: "no particular goal",
  targetedMuscleGroups: ["Everything"],
  availableEquipments: ["Everything"]
})

async function handleGenerateProgram() {
  generatedProgram.value = await generate_program(
    {
      programDuration: filters.value.programDuration,
      programDifficulty: filters.value.programDifficulty,
      programGoal: filters.value.programGoal,
      targetedMuscleGroups: filters.value.targetedMuscleGroups,
      availableEquipments: filters.value.availableEquipments
    }
  )
}

</script>

<style scoped>


</style>