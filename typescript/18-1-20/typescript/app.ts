let edad:number = 19;
let divMensaje : Element = document.querySelector('#mensaje');

function getFecha():string{
    return new Date().toString();
}

function sumar(a:number,b:number) :number{
    return  a+b;
}

function getEdad5Years():number{
    return sumar(edad,5);
}

divMensaje.innerHTML = getFecha();