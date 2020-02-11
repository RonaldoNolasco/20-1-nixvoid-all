import requests as r
from bs4 import BeautifulSoup
#Para que no aparezca la advertencia de que no tiene certificado HTTPS
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def obtenerLetraCodigoUNI(codigoUNI):
    cod = str(codigoUNI)
    arr = [2,1,2,3,4,5,6,7]
    suma = 0
    for i in range(len(cod)):
        suma += int(cod[i]) * arr[i]
    return chr(65 + suma % 11)

class spec:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
"""
cad="hola amigos que tal"
x=cad.split()
print(type(x))
a=[2,4]
print(type(a))
def arreg(cad):
    x=cad.split()
    comp='spec("' + x[0] +'", "'
    for m in range(1,len(x)):
        if(i==1):
            comp = comp + x[i]
        else:
            comp = comp + ' ' + x[i]
    comp = comp + '"),'
    return (comp)
"""
#x = spec("1", "2")
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

valido=True
for i in range(0,10):
    if (i==0 or i==1):
        valido=True
    elif (i==6 or i==8):
        continue
    for j in range(0,10):
        if(i==2 or i==3 or i==4 or i==5 or i==7 or i==9):
            if(j<5):
                valido=True
            else:
                valido=True
        for k in range(0,10):
            for l in range(0,10):
                test=""
                cod=""
                if(valido):
                    codigosl="2019"+str(i)+str(j)+str(k)+str(l)
                    codigo=codigosl + obtenerLetraCodigoUNI(int(codigosl))
                    url = "https://www.orce.uni.edu.pe/detaalu.php?id="+codigo+"&op=detalu"
                    response = r.get(url, verify=False)
                    response.encoding = 'utf-8'
                    soup = BeautifulSoup(response.text, 'html.parser')
                    x = soup.tbody.find_all('tr')[5]
                    add = soup.tbody.find_all('tr')[9]
                    tds = x.find_all('td')
                    tdadd = add.find_all('td')
                    test = str(tds[1].string)
                    testadd = str(tdadd[1].string)
                    if(test!="None"): 
                        for p in array:
                                if(p.nombre==testadd):
                                    cod=p.codigo
                        print(codigo + " " + cod + " " + test)
                        #print(codigo + ", " + cod + ", " + test)
                    else:
                        if(((i==0 or i==1) and j==0 and k==0 and l==0) or ((i==2 or i==3 or i==4 or i==5 or i==7 or i==9) and j==0 and k==0 and l==0) or ((i==2 or i==3 or i==4 or i==5 or i==7 or i==9) and j==5 and k==0 and l==0)): valido=True
                        else: valido=False
#Usar esta pagina: https://www.online-utility.org/text/sort.jsp para invertirlo y luego se agrega
#a la otra lista