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

arr=[]
valido=True
for i in range(2,10):
    if (i==0 or i==1):
        valido=True
        for j in range(0,10):
            for k in range(0,10):
                for l in range(0,10):
                    if(valido):
                        codigosl="2019"+str(i)+str(j)+str(k)+str(l)
                        codigo=codigosl + obtenerLetraCodigoUNI(int(codigosl))
                        url = "https://www.orce.uni.edu.pe/detaalu.php?id="+codigo+"&op=detalu"
                        response = r.get(url, verify=False)
                        response.encoding = 'utf-8'
                        soup = BeautifulSoup(response.text, 'html.parser')
                        x = soup.tbody.find_all('tr')[5]
                        tds = x.find_all('td')
                        test=str(tds[1].string)
                        if(test!="None"): print(codigo)
                        else:
                            if((i==0 or i==1) and j==0 and k==0 and l==0): valido=True
                            else: valido=False
    elif (i==6 or i==8):
        continue
    else:
        for j in range(0,10):
            if(j<5):
                valido=True
                for k in range(6,10):
                    for l in range(0,10):
                        if(valido):
                            codigosl="2019"+str(i)+str(j)+str(k)+str(l)
                            codigo=codigosl + obtenerLetraCodigoUNI(int(codigosl))
                            url = "https://www.orce.uni.edu.pe/detaalu.php?id="+codigo+"&op=detalu"
                            response = r.get(url, verify=False)
                            response.encoding = 'utf-8'
                            soup = BeautifulSoup(response.text, 'html.parser')
                            x = soup.tbody.find_all('tr')[5]
                            tds = x.find_all('td')
                            test=str(tds[1].string)
                            if(test!="None"): print (codigo)
                            else:
                                if((i==2 or i==3 or i==4 or i==5 or i==7 or i==9) and j==0 and k==0 and l==0): valido=True
                                else: valido=False
            else:
                valido=True
                for k in range(0,10):
                    for l in range(0,10):
                        if(valido):
                            codigosl="2019"+str(i)+str(j)+str(k)+str(l)
                            codigo=codigosl + obtenerLetraCodigoUNI(int(codigosl))
                            url = "https://www.orce.uni.edu.pe/detaalu.php?id="+codigo+"&op=detalu"
                            response = r.get(url, verify=False)
                            response.encoding = 'utf-8'
                            soup = BeautifulSoup(response.text, 'html.parser')
                            x = soup.tbody.find_all('tr')[5]
                            tds = x.find_all('td')
                            test=str(tds[1].string)
                            if(test!="None"): print (codigo)
                            else: 
                                if((i==2 or i==3 or i==4 or i==5 or i==7 or i==9) and j==5 and k==0 and l==0): valido=True
                                else:valido=False