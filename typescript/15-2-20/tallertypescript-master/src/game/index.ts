import { Jugador } from '../models/jugador';
import { TipoJugador } from '../models/tipoJugador';
import enumParserTipoJugador from '../utils/parser';

let listaJugadores: Array<Jugador> = [
  new Jugador('Monica', 140, TipoJugador.general),
  new Jugador('Fred', 310, TipoJugador.medico),
  new Jugador('Leonardo', 210, TipoJugador.medico),
  new Jugador('Jackie', 450, TipoJugador.general),
  new Jugador('Fiorella', 310, TipoJugador.medico),
  new Jugador('Sofia', 340, TipoJugador.guerrero)
];
function jugar() {
  let listaOrdenada: Array<Jugador> = listaJugadores.sort((a, b) => b.nivelPoder - a.nivelPoder);
  let ganador: Jugador = listaOrdenada[Math.floor(Math.random()*4)];
  ganador.incrementarNivel();
  let textGanador: HTMLParagraphElement = document.querySelector('#textoGanador');
  actualizarListaJugadores();
  textGanador.innerText = `El ganador del juego es: ${ganador.nombre}`;
}
function agregarJugador() {
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
  agregarJugadorALaLista(jugador);
}
function agregarJugadorALaLista(jugador: Jugador):void {
  listaJugadores.push(jugador);
  actualizarListaJugadores();
}
function actualizarListaJugadores():void {
  let listaHTML: HTMLUListElement = document.querySelector('#listaJugadores');
  listaHTML.innerHTML = '';
  for(let jugador of listaJugadores) {
      let liJugador = document.createElement('li');
      liJugador.innerText = `${jugador.nombre} (${jugador.tipoJugador}): ${jugador.nivelPoder}`;
      listaHTML.append(liJugador);
  }
}

export {
  jugar,
  agregarJugador,
  actualizarListaJugadores
}