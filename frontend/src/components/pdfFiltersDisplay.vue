<template>

<div class="filter-container">

    <div class="filter-container-row">
        <label for="programName">Program's name:</label>
        <input type="text" id="programName" v-model="pdfFilters.programName" maxlength="40">
    </div>

    <div class="filter-container-row">
        <label for="showDescriptions" >Show Descriptions in PDF:</label>
        <input type="checkbox" id="showDescriptions" v-model="pdfFilters.showDescriptions">
    </div>

</div>

</template>

<script setup>

const pdfFilters = defineModel()

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
    display: inline;
    gap: 1rem 1rem;
    flex-wrap: wrap;
    padding: 1%;
}

.filter-container-row {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    flex-wrap: nowrap;
    padding: 0.5%;
}

</style>