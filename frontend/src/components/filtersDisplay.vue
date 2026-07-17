<template>

    <h4>Basic parameters</h4>

    <div class="filter-container">
        <div class="filter-container-row">
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
        </div>

        <div class="filter-container-row">
            <label for="levelFilter">Experience: </label>
            <select name="levelFilter" id="levelFilter">
                <option value="1">Just started</option>
                <option value="2">Beginner</option>
                <option value="3">Intermediate</option>
                <option value="4">Advanced</option>
            </select>
        </div>

        <div class="filter-container-row">
            <label for="goal">Goal: </label>
            <select name="goal" id="goal">
                <option value="1">No particular goal</option>
                <option value="1">Muscle gain</option>
                <option value="2">Strength training</option>
                <option value="3">Endurance</option>
            </select>
        </div>

    </div>

    <h4>
        targeted muscle groups
        <span>
        <button @click="showMuscleGroups = !showMuscleGroups">
        {{ showMuscleGroups ? "▼" : "▶" }}
        </button>
    </span>
    </h4>

    <div class="checkbox-group" v-if="showMuscleGroups">
        <label v-for="item in muscleGroupsOptions" :key="item" class="checkbox-label">
            <input type="checkbox" :value="item" v-model="muscleGroups" @change="toggleMuscleGroup(item)" />

            {{ item }}

        </label>
    </div>

    <h4>
        Available equipment
        <span>
        <button @click="showEquipment = !showEquipment">
        {{ showEquipment ? "▼" : "▶" }}
        </button>
    </span>
    </h4>

    <div class="checkbox-group" v-if="showEquipment">
        <label v-for="item in availableEquipmentOptions" :key="item" class="checkbox-label">
            <input type="checkbox" :value="item" v-model="availableEquipment" @change="toggleAvailableEquipment(item)" />

            {{ item }}

        </label>
    </div>

        <p>Selected muscle groups:</p>
        <pre>{{ muscleGroups }}</pre>

        <p>Selected available equipment:</p>
        <pre>{{ availableEquipment }}</pre>

</template>

<script setup>
import { ref } from "vue"

const muscleGroups = ref(["Everything"])
const availableEquipment = ref(["Everything"])

const showEquipment = ref(false)
const showMuscleGroups = ref(false)

const muscleGroupsOptions = [
    "Everything",
    "Chest",
    "Shoulders and traps",
    "Arms",
    "Back",
    "Legs",
    "Core"
]

const availableEquipmentOptions = [
    "Everything",
    "Nothing (bodyweight only)",
    "Dumbbells",
    "Barbells",
    "Kettlebells",
    "Cable machines",
    "Pulley machines",
    "Weights machines",
    "Platforms",
    "Squat racks",
    "Benches",
    "Resistance bands",
    "Pull-up bars",
    "Medicine balls",
]

function toggleMuscleGroup(item) {
    if (item === 'Everything') {
        muscleGroups.value = ['Everything']
    } else {
        muscleGroups.value = muscleGroups.value.filter(
            group => group !== 'Everything'
        )
    }
}

function toggleAvailableEquipment(item) {
    if (item === 'Everything') {
        availableEquipment.value = ['Everything']
    } else if (item === 'Nothing (bodyweight only)') {
        availableEquipment.value = ['Nothing (bodyweight only)']
    } else {
        availableEquipment.value = availableEquipment.value.filter(
            equip => equip !== 'Everything'
        )
        availableEquipment.value = availableEquipment.value.filter(
            equip => equip !== 'Nothing (bodyweight only)'
        )
    }
}

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

.filter-container {
    display: flex;
    gap: 1rem 1rem;
    flex-wrap: wrap;
}

.filter-container-row {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    flex-wrap: nowrap;
}

</style>