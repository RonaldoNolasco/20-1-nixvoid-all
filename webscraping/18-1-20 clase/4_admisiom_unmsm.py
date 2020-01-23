import requests as r
from bs4 import BeautifulSoup

# 4 kind of objects Tag, NavigableString, BeautifulSoup, and Comment
url = "http://unmsm.claro.net.pe/ResultSDP20201/1/0611/0.html"

# . <- navigable object

response = r.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())

# contents

# print(soup.table.tbody)
print("--------------------------------------------")
#print(soup.tbody)
#print("THEY'RE THE SAME")

#Mostrarlo como csv

"""
for tr in soup.table.tbody:
    for td in tr:
        print(td.text, end=' ')
    print()
    #break
"""

#Mostrarlo como json
"""
resultados = []

for tr in soup.table.tbody:
  importantes = tr.find_all('td')[:6]
  sede,codigo,nombre,trash,puntaje,merito = importantes
  resultados.append({
    "codigo": codigo.text,
    "nombre": nombre.text,
    "puntaje": puntaje.text,
    "merito": merito.text
  })

print(resultados)
"""

#Funcion buscador

"""
def buscar(name):
  for postulante in resultados:
    if postulante["nombre"].find(name) != -1:
      print("Encontrado: " + postulante["nombre"])

buscar("BRISEIDA")
"""