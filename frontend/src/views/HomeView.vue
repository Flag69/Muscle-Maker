<template>
  <h1>Muscle Maker</h1>

  <!-- Div to place filters -->
  <div></div>

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

const generatedProgram = ref(null)

async function handleGenerateProgram() {
  generatedProgram.value = await generate_program()
}

</script>

<style scoped>

.button {
    background-color: #4CAF50;
    border: none;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 4px;
}

</style>