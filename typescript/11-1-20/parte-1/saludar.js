/*function saludar(nombre){
    var saludo='Hola, ';
    console.log(saludo+nombre);
}
saludar('GAAAAAAAA');
*/

let nombre='Ronaldo Nolasco';
//console.log(typeof (nombre));

let mayoriaDeEdad = 18;
//console.log(typeof (mayoriaDeEdad));

const notas = [18,19,20];
//console.log(notas.length);
//notas=[1,1,1];

/*
for(let i=0;i<3;i++) notas[i]=1;
*/

//console.log(notas);

//para borrar -> delete variable

let alumnos = [
    {
        codigo: '20151216G',
        clave: '325244'
    },
    {
        codigo: '20183347A',
        clave: '357612'
    },
    {
        codigo: '20163121F',
        clave: '975362'
    }
];

function corredor(a){
    console.log(a.codigo + '-' + a.clave);
}

alumnos.forEach(corredor);

////Si se borra el package-lock y el node_modules, se puede volver a instalar todo con npm install
