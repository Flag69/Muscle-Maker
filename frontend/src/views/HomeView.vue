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

  <!-- Div to place pdf download button -->
  <div v-if="generatedProgram">
    <pdfButton @generatePdf="handleGeneratePdf" />

      <pdfFiltersDisplay v-model="pdfFilters" />  
  </div>

</template>

<script setup>
import { ref } from "vue"
import { generate_program, generate_pdf } from "@/services/api"
import generateButton from "@/components/generateButton.vue"
import pdfButton from "@/components/pdfButton.vue"
import programDisplay from "@/components/programDisplay.vue"
import filtersDisplay from "@/components/filtersDisplay.vue"
import pdfFiltersDisplay from "@/components/pdfFiltersDisplay.vue"

const generatedProgram = ref(null)

const showFilters = ref(false)

const filters = ref({
  programDuration: 60,
  programDifficulty: 4,
  programGoal: "no particular goal",
  targetedMuscleGroups: ["Everything"],
  availableEquipments: ["Everything"]
})

const pdfFilters = ref({
  programName: "Amazing workout program",
  showDescriptions: true,
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

async function handleGeneratePdf() {
  await generate_pdf(generatedProgram.value, pdfFilters.value)
}

</script>

<style scoped>

h1 {
  font-size: 1.6rem;
}


</style>