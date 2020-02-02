<template>
    <div class="app">
        <!-- <input type="number" v-model="num"> 
        {{retornar(num)}}
        <br><br>
        {{notas[0]}}
        <br><br>
        {{alumno.nombre}}
        <br><br>
        <div>
            <span v-bind:title="mensaje">{{salida}}</span>
        </div>
        <ul>
            <li>nombre: {{alumno.nombre}}</li>
            <li>apellido: {{alumno.apellido}}</li>
            <li>codigo: {{alumno.codigo}}</li>
            <li>imagen: {{alumno.imagen}}</li>
        </ul>
        <img :src="alumno.imagen"> -->

        <!-- <button @click="cpp=!cpp">Si o no</button>
        <p v-if="cpp">Vas a caer ctm</p>
        <p v-else>Que chucha miras causa</p> -->

        <!-- si se cumple la 1ra linea, no se cumple ninguna de las demás, y si no, puede cumplirse
        la 2da o la 3ra -->
        <!-- <div v-if="!cpp">Vas a caer ctm</div>
        <div v-else-if="numeroOrden>18">Hay alumnos</div>
        <div v-else>No hay alumnos</div> -->

        <!-- <p v-show="cpp">Vas a caer ctm</p>
        <p v-for="nota in notas" :key=nota>{{nota}}</p> -->

        <!-- <div v-for="alumno in alumnos" :key="alumno.codigo" class="alumnoEnLista">
            <div v-if="alumno.condicionNormal && alumno.cicloRelativo">
                <p>Nombre completo: {{alumno.nombre + " " + alumno.apellido}}</p>
                <p>Codigo: {{alumno.codigo}}</p>
                <p>Ciclo relativo: {{alumno.cicloRelativo}}</p>
                <p>Imagen:</p>
                <img src="https://www.dictionary.com/e/wp-content/uploads/2018/03/waifu.jpg" width="200px">
            </div>
        </div> -->

        <!-- <div v-for="(alumno, index) in alumnos" :key="index">
            <div v-if="alumno.condicionNormal && alumno.cicloRelativo">
                <p>{{index}}</p>
                <p>Nombre completo: {{alumno.nombre + " " + alumno.apellido}}</p>
                <p>Codigo: {{alumno.codigo}}</p>
                <p>Ciclo relativo: {{alumno.cicloRelativo}}</p>
                <p>Imagen:</p>
                <img src="https://www.dictionary.com/e/wp-content/uploads/2018/03/waifu.jpg" width="200px">
            </div>
        </div> -->

        <!-- <div v-for="(data, propiedad) in alumno" :key="propiedad">
            <h1>{{propiedad+": "+ data}}</h1>
        </div> -->
        <input v-model="text"> {{text}}
        <br><br>
        <h1>{{message}}</h1>
        <button @click="reverseMessage">Reverse</button>
        
        
    </div>
</template>

<script>
export default {
    name: 'App',
    data(){
        return{
            // salida:"Hello World",
            // num: 12,
            // notas: [24,17,16],
            // alumno: {
            //     nombre: 'Ronaldo',
            //     apellido: 'Nolasco',
            //     codigo: '20180125F',
            //     imagen: 'https://i.pinimg.com/originals/31/a9/eb/31a9eb82d9805a090cceaf92e538beb7.jpg'
            // },
            // mensaje: "Vas a caer bonillizi",
            // cpp: true,
            // numeroOrden: 20,
            // alumnos: [
            //     {
            //         codigo: '20',
            //         nombre: 'Ronaldo',
            //         apellido: 'Nolasco',
            //         condicionNormal: true,
            //         cicloRelativo: 5,
            //         imagen: 'https://d500.epimg.net/cincodias/imagenes/2018/11/13/lifestyle/1542113135_776401_1542116070_noticia_normal.jpg'
            //     },
            //     {
            //         codigo: '21',
            //         nombre: 'Cristhian',
            //         apellido: 'Bonilla',
            //         condicionNormal: false,
            //         cicloRelativo: 4,
            //         imagen: 'https://d500.epimg.net/cincodias/imagenes/2018/11/13/lifestyle/1542113135_776401_1542116070_noticia_normal.jpg'
            //     },
            //     {
            //         codigo: '22',
            //         nombre: 'Juan',
            //         apellido: 'Alva',
            //         condicionNormal: false,
            //         cicloRelativo: 4,
            //         imagen: 'https://d500.epimg.net/cincodias/imagenes/2018/11/13/lifestyle/1542113135_776401_1542116070_noticia_normal.jpg'
            //     },
            //     {
            //         codigo: '23',
            //         nombre: 'Franz',
            //         apellido: 'Bendezu',
            //         condicionNormal: true,
            //         cicloRelativo: 5,
            //         imagen: 'https://d500.epimg.net/cincodias/imagenes/2018/11/13/lifestyle/1542113135_776401_1542116070_noticia_normal.jpg'
            //     },
            //     {
            //         codigo: '24',
            //         nombre: 'Rosa',
            //         apellido: 'Ginocchio',
            //         condicionNormal: false,
            //         cicloRelativo: 4,
            //         imagen: 'https://d500.epimg.net/cincodias/imagenes/2018/11/13/lifestyle/1542113135_776401_1542116070_noticia_normal.jpg'
            //     },
            //     {
            //         codigo: '25',
            //         nombre: 'Juan',
            //         apellido: 'Napan',
            //         condicionNormal: false,
            //         cicloRelativo: 3,
            //         imagen: 'https://d500.epimg.net/cincodias/imagenes/2018/11/13/lifestyle/1542113135_776401_1542116070_noticia_normal.jpg'
            //     },
            //     {
            //         codigo: '26',
            //         nombre: 'Jose',
            //         apellido: 'Ñiquen',
            //         condicionNormal: false,
            //         cicloRelativo: 3,
            //         imagen: 'https://d500.epimg.net/cincodias/imagenes/2018/11/13/lifestyle/1542113135_776401_1542116070_noticia_normal.jpg'
            //     },
            //     {
            //         codigo: '27',
            //         nombre: 'Brenda',
            //         apellido: 'Marcos',
            //         condicionNormal: false,
            //         cicloRelativo: 4,
            //         imagen: 'https://d500.epimg.net/cincodias/imagenes/2018/11/13/lifestyle/1542113135_776401_1542116070_noticia_normal.jpg'
            //     },
            //     {
            //         codigo: '28',
            //         nombre: 'Carol',
            //         apellido: 'G',
            //         condicionNormal: true,
            //         cicloRelativo: 5,
            //         imagen: 'https://d500.epimg.net/cincodias/imagenes/2018/11/13/lifestyle/1542113135_776401_1542116070_noticia_normal.jpg'
            //     },
            //     {
            //         codigo: '29',
            //         nombre: 'Jorgito',
            //         apellido: 'Luna',
            //         condicionNormal: true,
            //         cicloRelativo: 5,
            //         imagen: 'https://d500.epimg.net/cincodias/imagenes/2018/11/13/lifestyle/1542113135_776401_1542116070_noticia_normal.jpg'
            //     },
            // ]
            // alumno:{
            //     nombre: 'Ronaldo',
            //     apellido: 'Nolasco',
            //     codigo: '20180125F',
            //     imagen: 'https://i.pinimg.com/originals/31/a9/eb/31a9eb82d9805a090cceaf92e538beb7.jpg'
            // }
            text: '',
            message: 'Hello Vue!'
        }
    },
    methods: {
        retornar(num){
            return (Number(this.num) + 5)
        },
        reverseMessage: function () {
            this.message = this.message.split('').reverse().join('')
    }
    },
}
</script>

<style>
.app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
}
</style>