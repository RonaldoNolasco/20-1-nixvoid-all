import requests as r
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def obtenerCodigoUNI(codigoUNI):
    cod = str(codigoUNI)
    arr = [2,1,2,3,4,5,6,7]
    suma = 0
    for i in range(len(cod)):
        suma += int(cod[i]) * arr[i]
    return (cod + chr(65 + suma % 11))

class spec:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
print(3/2)
        
array=[
    spec("A1", "ARQUITECTURA"),
    spec("C1", "INGENIERÍA CIVIL"),
    spec("E1", "INGENIERÍA ECONÓMICA"),
    spec("E3", "INGENIERÍA ESTADÍSTICA"),
    spec("G1", "INGENIERÍA GEOLÓGICA"),
    spec("G2", "INGENIERÍA METALÚRGICA"),
    spec("G3", "INGENIERÍA DE MINAS"),
    spec("I1", "INGENIERÍA INDUSTRIAL"),
    spec("I2", "INGENIERÍA DE SISTEMAS"),
    spec("L1", "INGENIERÍA ELÉCTRICA"),
    spec("L2", "INGENIERÍA ELECTRÓNICA"),
    spec("L3", "INGENIERÍA DE TELECOMUNICACIONES"),
    spec("M3", "INGENIERÍA MECÁNICA"),
    spec("M4", "INGENIERÍA MECÁNICA Y ELÉCTRICA"),
    spec("M5", "INGENIERÍA NAVAL"),
    spec("M6", "INGENIERÍA MECATRÓNICA"),
    spec("N1", "FÍSICA"),
    spec("N2", "MATEMÁTICA"),
    spec("N3", "QUÍMICA"),
    spec("N5", "INGENIERÍA FÍSICA"),
    spec("N6", "CIENCIA DE LA COMPUTACIÓN"),
    spec("P2", "INGENIERÍA PETROQUÍMICA"),
    spec("P3", "INGENIERÍA DE PETRÓLEO Y GAS NATURAL"),
    spec("Q1", "INGENIERÍA QUÍMICA"),
    spec("Q2", "INGENIERÍA TEXTIL"),
    spec("S1", "INGENIERÍA SANITARIA"),
    spec("S2", "INGENIERÍA DE HIGIENE Y SEGURIDAD INDUSTRIAL"),
    spec("S3", "INGENIERÍA AMBIENTAL"),
    ]

for i in range (0,10000,500):
    for j in range(i,i+500):
        codigo=obtenerCodigoUNI(2019*10000 + j)
        url = "https://www.orce.uni.edu.pe/detaalu.php?id="+codigo+"&op=detalu"
        response = r.get(url, verify=False)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        nombrer = soup.tbody.find_all('tr')[5]
        codespr = soup.tbody.find_all('tr')[9] # bs4.element.Tag
        nombred = nombrer.find_all('td')
        codespd = codespr.find_all('td') # bs4.element.ResultSet
        nombre = str(nombred[1].string)
        codesp = str(codespd[1].string) #bs4.element.String to str
        if(nombre!="None"):
            for esp in array:
                if(esp.nombre==codesp):
                    codigoesp=esp.codigo
                    nombreesp=esp.nombre
                    break
            print(codigo + " " + codigoesp + " " + nombreesp)
        elif(nombre=="None" and j%500!=0): 
            break