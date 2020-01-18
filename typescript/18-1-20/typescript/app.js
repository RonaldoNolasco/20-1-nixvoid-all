var edad = 19;
var divMensaje = document.querySelector('#mensaje');
function getFecha() {
    return new Date().toString();
}
function sumar(a, b) {
    return a + b;
}
function getEdad5Years() {
    return sumar(edad, 5);
}
divMensaje.innerHTML = getFecha();
