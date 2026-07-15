<template>
    <label for="durationFilter">Program's duration: </label>
    <select name="durationFilter" id="durationFilter">
        <option value="30">30 minutes</option>
        <option value="45">45 minutes</option>
        <option value="60">1 hour</option>
        <option value="75">1 hour 15 minutes</option>
        <option value="90">1 hour 30 minutes</option>
        <option value="105">1 hour 45 minutes</option>
        <option value="120">2 hours</option>
    </select>

    <label for="levelFilter">Experience : </label>
    <select name="levelFilter" id="levelFilter">
        <option value="1">Just started</option>
        <option value="2">Beginner</option>
        <option value="3">Intermediate</option>
        <option value="4">Advanced</option>
    </select>

  <h2>Equipment Available</h2>

  <label>
    <input
      type="checkbox"
      value="Barbell"
      v-model="equipment"
    />
    Barbell
  </label>

  <br>

  <label>
    <input
      type="checkbox"
      value="Dumbbells"
      v-model="equipment"
    />
    Dumbbells
  </label>

  <br>

  <label>
    <input
      type="checkbox"
      value="Machines"
      v-model="equipment"
    />
    Machines
  </label>

  <br>

  <label>
    <input
      type="checkbox"
      value="Bodyweight"
      v-model="equipment"
    />
    Bodyweight
  </label>

  <p>Selected equipment:</p>
  <pre>{{ equipment }}</pre>

</template>

<script setup>
import { ref } from "vue"

const equipment = ref([])

</script>

<style scoped> 
</style>