import { agregarJugador, jugar, actualizarListaJugadores} from './src/game/index';

let btnAgregarJugador: HTMLElement = document.querySelector('#btnAgregarJugador');
let btnJugar: HTMLElement = document.querySelector('#btnJugar');

btnAgregarJugador.onclick = agregarJugador;
btnJugar.onclick = jugar;
actualizarListaJugadores();