<template>
    <!-- Es recomendable que la clase tenga el mismo nombre que el componente-->
    <div class="card">
        <div class="card-image">
            <img :src="imgUrl" alt="usuario">
        </div>
        <div class="card-description">
            <div>
                <p>Nombres: {{nombres}}</p>
                <p>Apellidos: {{apellidos}}</p>
                <p>Ciclo: {{cicloRelativo}}</p>
                <p>Codigo: {{codigo}}</p>
                <p>Especialidad: {{especialidad}}</p>
                <p>Facultad: {{facultad}}</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Card',
    //Sirve para inicializarlo sin ningun valor
    props:{
        nombres: String,
        apellidos: String,
        cicloRelativo: Number,
        imgUrl: String,
        codigo: String,
        especialidad: String,
        facultad: String
    }
}
</script>

<style lang="scss">
.card{
    display: flex; //Para que se muestre la imagen al costado
    flex-direction: row; 
    border: 2px red solid; //Longitud, color y tipo de borde
    border-radius: 15px;//Bordes redondeados
    align-items: center;
    .card-image{
        display: flex;
        flex-direction: row;
        //flex-grow: 1;
        justify-content: center;
        flex-basis: 50%; //Darle el 50% del ancho
    }
    .card-description{
        display: flex;
        flex-direction: column;
        justify-content: center;
        flex-basis: 50%
    }
}
</style>