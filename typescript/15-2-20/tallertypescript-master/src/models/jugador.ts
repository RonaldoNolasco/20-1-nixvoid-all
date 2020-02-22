import { TipoJugador } from './tipoJugador';

export class Jugador {
  nombre: string
  nivelPoder: number
  tipoJugador: TipoJugador
  constructor(nombre: string, nivelPoder: number, tipoJugador: TipoJugador) {
      this.nombre = nombre;
      this.nivelPoder = nivelPoder;
      this.tipoJugador = tipoJugador;
  }
  incrementarNivel(): void {
      this.nivelPoder += 10;
  }
}