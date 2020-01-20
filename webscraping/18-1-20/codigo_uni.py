def obtenerLetraCodigoUNI(codigoUNI):
    cod = str(codigoUNI)
    arr = [2,1,2,3,4,5,6,7]
    suma = 0
    for i in range(len(cod)):
        suma += int(cod[i]) * arr[i]
    return chr(65 + suma % 11)

print(obtenerLetraCodigoUNI(20151216))
