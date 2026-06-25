<template>
    <button @click="$emit('generateProgram')">Generate program</button>
</template>

<script setup>

defineEmits(['generateProgram'])

</script>

<style scoped>

button {
    background-color: #94e697;
    border: 1px solid black;
    color: rgb(0, 0, 0);
    padding: 15px 32px;
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
    background-color: #4CAF50;
    color: white;
}

button:active {
    box-shadow: 2px 2px #194e1b;
    transform: translateY(4px);
}

</style>