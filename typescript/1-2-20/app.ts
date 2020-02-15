//Se tiene que poner el enum arriba de todo
//Cuidado al declarar arreglos, tienen que igualarse a []

enum TipoJugador {
    guerrero = 'guerrero',
    medico = 'medico',
    general = 'general'
}

let listaJugadores: Array<Jugador> = [
    /*
    {
        nombre: "Ronaldo",
        nivelPoder: 20,
        tipoJugador: TipoJugador.guerrero
    },
    {
        nombre: "Juan",
        nivelPoder: 18,
        tipoJugador: TipoJugador.general
    },
    {
        nombre: "Cristhian",
        nivelPoder: 15,
        tipoJugador: TipoJugador.medico
    },
    {
        nombre: "Jorge",
        nivelPoder: 8,
        tipoJugador: TipoJugador.guerrero
    },
    {
        nombre: "Franz",
        nivelPoder: 5,
        tipoJugador: TipoJugador.medico
    },
    */
];
let btnAgregarJugador: HTMLElement = document.querySelector('#btnAgregarJugador');
let btnJugar: HTMLElement = document.querySelector('#btnJugar');
let btnActualizar: HTMLElement = document.querySelector('#btnActualizar');

class Jugador {
    nombre: string
    nivelPoder: number
    tipoJugador: TipoJugador
    constructor(nombre: string, nivelPoder: number, tipoJugador: TipoJugador) {
        this.nombre = nombre;
        this.nivelPoder = nivelPoder;
        this.tipoJugador = tipoJugador;
    }
}

function getRandomInt(max) {
    return Math.floor(Math.random() * Math.floor(max));
  }

function jugar() {
    let listaOrdenada: Array<Jugador> = listaJugadores
    listaOrdenada.sort((a, b) => a.nivelPoder - b.nivelPoder).reverse();
    //listaOrdenada.sort((a, b) => b.nivelPoder - a.nivelPoder);
    let indice = getRandomInt(3);
    let ganadorHTML: HTMLUListElement = document.querySelector('#ganador');
    ganadorHTML.innerHTML = '';
    let liJugadorGanador = document.createElement('li');
    liJugadorGanador.innerText = 'El ganador es: ' + listaOrdenada[indice].nombre;
    ganadorHTML.append(liJugadorGanador)
}

function agregarJugador(jugador: Jugador):void {
    listaJugadores.push(jugador);
    actualizarListaJugadores();
}

function actualizarListaJugadores():void {
    let listaHTML: HTMLUListElement = document.querySelector('#listaJugadores');
    listaHTML.innerHTML = '';
    for(let jugador of listaJugadores) {
        let liJugador = document.createElement('li');
        liJugador.innerText = jugador.nombre + ' - ' + jugador.nivelPoder + ' - ' + jugador.tipoJugador;
        listaHTML.append(liJugador);
    }
}

let enumParserTipoJugador: Object = {
    'guerrero': TipoJugador.guerrero,
    'medico': TipoJugador.medico,
    'general': TipoJugador.general
};

btnAgregarJugador.onclick = function () {
    let inputNombre: HTMLInputElement = document.querySelector('#inputNombre');
    let inputNivelPoder: HTMLInputElement = document.querySelector('#inputNivelPoder');
    let selectTipoJugador: HTMLSelectElement = document.querySelector('#selectTipoJugador');
    let jugador: Jugador = new Jugador(
        inputNombre.value,
        Number(inputNivelPoder.value),
        enumParserTipoJugador[selectTipoJugador.value]
    );
    inputNombre.value = '';
    inputNivelPoder.value = '';
    selectTipoJugador.value = 'guerrero';
    agregarJugador(jugador);
}

btnJugar.onclick = jugar;

btnActualizar.onclick = actualizarListaJugadores;