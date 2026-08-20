<template>
    <button @click="$emit('generatePdf')">Generate PDF</button>
</template>

<script setup>

defineEmits(['generatePdf'])

</script>

<style scoped>

button {
    background-color: #f38459;
    border: 1px solid black;
    color: rgb(255, 255, 255);
    padding: 12px 24px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 4px;
    box-shadow: 3px 3px #194e1b;
}

button:hover {
    background-color: #d4a6a6;
    color: rgb(255, 116, 116);
}

button:active {
    box-shadow: 2px 2px #194e1b;
    transform: translateY(4px);
}

</style>