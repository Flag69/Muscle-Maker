<template>

    <h4>Basic parameters</h4>

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

    <h4>Targeted muscle groups</h4>

        <div class="checkbox-group">
            <label v-for="item in musclegroupsOptions" :key="item" class="checkbox-label">
                <input type="checkbox" :value="item" v-model="musclegroups" />

                {{ item }}

            </label>
        </div>

        <p>Selected muscle groups:</p>
        <pre>{{ musclegroups }}</pre>

</template>

<script setup>
import { ref } from "vue"

const musclegroups = ref([])

const musclegroupsOptions = [
    "Everything",
    "Chest",
    "Shoulders and traps",
    "Arms",
    "Back",
    "Legs",
    "Core"
]

</script>

<style scoped> 

.checkbox-label {
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.checkbox-group {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(120px, 0.5fr));
    gap: 0.3rem 0.5rem;
}

</style>