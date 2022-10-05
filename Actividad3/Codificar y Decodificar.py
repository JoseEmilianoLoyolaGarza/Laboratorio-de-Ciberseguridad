import base64

def Decode1():
    file = open('C:/Users/logaa/Pictures/Facultad/TercerSemestre/Laboratorio/Actividad3/mystery_img1.txt', 'rb') 
    byte = file.read() 
    file.close()  
    decode = open('C:/Users/logaa/Pictures/Facultad/TercerSemestre/Laboratorio/Actividad3/mystery_img1.jpg', 'wb') 
    decode.write(base64.b64decode((byte))) 
    decode.close() 

def Decode2():
    file = open('C:/Users/logaa/Pictures/Facultad/TercerSemestre/Laboratorio/Actividad3/mystery_img2.txt', 'rb') 
    byte = file.read() 
    file.close()  
    decode = open('C:/Users/logaa/Pictures/Facultad/TercerSemestre/Laboratorio/Actividad3/mystery_img2.jpg', 'wb') 
    decode.write(base64.b64decode((byte))) 
    decode.close()
    
def CodeHello():
    file = open('C:/Users/logaa/Pictures/Facultad/TercerSemestre/Laboratorio/Actividad3/hola_mundo.c', 'rb') 
    byte = file.read() 
    file.close()  
    code = open('C:/Users/logaa/Pictures/Facultad/TercerSemestre/Laboratorio/Actividad3/hola_mundo.txt', 'wb') 
    code.write(base64.b64encode((byte))) 
    code.close()

CodeHello()
Decode1()
Decode2()