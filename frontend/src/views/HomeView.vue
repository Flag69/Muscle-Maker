<template>
  <h1>Muscle Maker</h1>

  <!-- Div to place filters -->
  <div></div>

  <!-- Div to place generation buttons -->
  <div>
    <button @click="handleGenerateProgram">Generate</button>
  </div>

  <!-- Div to display generated program -->
  <div v-if="generatedProgram">
    {{ generatedProgram }}
  </div> 

</template>

<script setup>
import { ref } from "vue"
import { generate_program } from "@/services/api"

const generatedProgram = ref()

async function handleGenerateProgram() {
  generatedProgram.value = await generate_program()
}

</script>

<style scoped>
</style>