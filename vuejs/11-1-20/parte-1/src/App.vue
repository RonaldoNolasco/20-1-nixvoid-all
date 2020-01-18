<template>
    <div>
        Hola mundo!
        <button @click="saludar">Chupetin</button>
    </div>
</template>

<script>
export default {
    name: 'app',
    methods: {
        saludar: function(){
            alert('hola');
        }
    },
}
</script>

<style lang="">
    
</style>