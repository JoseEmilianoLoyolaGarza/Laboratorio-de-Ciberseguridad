from ftplib import FTP
ftp = FTP('ftp.agmercados.com')  
  
ftp.login()   
ftp.dir()
Nom=ftp.nlst()
for a in Nom:
    try:
        ftp.retrbinary(f"RETR {a}", open("C:/Users/logaa/Pictures/Facultad/TercerSemestre/Laboratorio/Actividad7/TXT/"+a,"wb").write) 
    except:
        print("El archivo:"+str(a)+" no se pudo descargar")

ftp.cwd('Update')
Nom=ftp.nlst()
for a in Nom:
     try:
         ftp.retrbinary(f"RETR {a}", open("C:/Users/logaa/Pictures/Facultad/TercerSemestre/Laboratorio/Actividad7/TXT/"+a,"wb").write) 
     except:
         print("El archivo:"+str(a)+" no se pudo descargar") 
         
ftp.cwd('Temp')
Nom=ftp.nlst()
for a in Nom:
     try:
         ftp.retrbinary(f"RETR {a}", open("C:/Users/logaa/Pictures/Facultad/TercerSemestre/Laboratorio/Actividad7/TXT/"+a,"wb").write) 
     except:
         print("El archivo:"+str(a)+" no se pudo descargar")        

ftp.quit()