<template>
  <h1>Muscle Maker</h1>

  <!-- Div to place filters -->
  <div>
    <filtersDisplay />
  </div>

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

async function handleGenerateProgram() {
  generatedProgram.value = await generate_program()
}

</script>

<style scoped>


</style>