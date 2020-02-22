var listaJugadores = [];
var TipoJugador;
(function (TipoJugador) {
    TipoJugador["guerrero"] = "guerrero";
    TipoJugador["medico"] = "medico";
    TipoJugador["general"] = "general";
})(TipoJugador || (TipoJugador = {}));
var Jugador = /** @class */ (function () {
    function Jugador(nombre, nivelPoder, tipoJugador) {
        this.nombre = nombre;
        this.nivelPoder = nivelPoder;
        this.tipoJugador = tipoJugador;
    }
    Jugador.prototype.incrementarNivel = function () {
        this.nivelPoder += 10;
    };
    return Jugador;
}());
function jugar() {
}
function agregarJugador(jugador) {
    listaJugadores.push(jugador);
    actualizarListaJugadores();
}
function actualizarListaJugadores() {
    var listaHTML = document.querySelector('#listaJugadores');
    listaHTML.innerHTML = '';
    for (var _i = 0, listaJugadores_1 = listaJugadores; _i < listaJugadores_1.length; _i++) {
        var jugador = listaJugadores_1[_i];
        var liJugador = document.createElement('li');
        liJugador.innerText = jugador.nombre;
        listaHTML.append(liJugador);
    }
}
var btnAgregarJugador = document.querySelector('#btnAgregarJugador');
var enumParserTipoJugador = {
    'guerrero': TipoJugador.guerrero,
    'medico': TipoJugador.medico,
    'general': TipoJugador.general
};
btnAgregarJugador.onclick = function () {
    var inputNombre = document.querySelector('#inputNombre');
    var inputNivelPoder = document.querySelector('#inputNivelPoder');
    var selectTipoJugador = document.querySelector('#selectTipoJugador');
    var jugador = new Jugador(inputNombre.value, Number(inputNivelPoder.value), enumParserTipoJugador[selectTipoJugador.value]);
    agregarJugador(jugador);
};
