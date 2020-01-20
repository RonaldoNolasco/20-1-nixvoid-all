function obtenerLetraCodigoUNI(codigoUNI /*solo números*/) {
    let cod = String(codigoUNI);
    let sum = 0;
    const arr = [2, 1, 2, 3, 4, 5, 6, 7];
    for (let i = 0; i < cod.length; i++) {
        sum += cod.charAt(i) * arr[i];
    }
    return String.fromCharCode(65 + sum % 11);
}

console.log(obtenerLetraCodigoUNI(20151216));
