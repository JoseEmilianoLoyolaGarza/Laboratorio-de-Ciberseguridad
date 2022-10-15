from  bs4 import BeautifulSoup
import requests

url="https://www.20minutos.com.mx/minuteca/nuevo-leon/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
eq = soup.find_all("div",class_="media-intro")
tit = soup.find_all("h1")
aut= soup.find_all("div",class_="author")


info=list()
titulos=list()
autor=list()

count = 0
for i in aut:
    if count < 20:
        autor.append(i.text)
    else:
        break
    count += 1

count = 0
for i in eq:
    if count < 20:
        info.append(i.text)
    else:
        break
    count += 1

count = 0
for i in tit:
    if count < 21:
        titulos.append(i.text)
    else:
        break
    count += 1
   
titulos.pop(0)

archivo = open("C:/Users/logaa/Pictures/Facultad/TercerSemestre/Laboratorio/Actividad4/datos.txt", "w")
for i in range(20):
    archivo.write(str(titulos[i]))
    archivo.write(str(info[i]))
    archivo.write(str(autor[i]))
archivo.close()