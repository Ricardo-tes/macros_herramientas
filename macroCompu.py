import pyautogui
from time import sleep
import csv
# Este programa es una macro que abre el navegador...

AREA_POSTULACIONES = (806, 171, 854, 857) 
#Sector de la pantalla donde se realizar
AREA_ANUNCIOS = (334, 297, 533, 746)

#Entra a la página computrabajo, comprueba que esté logueado y si no lo está se loguea
def entrar():
    
    pyautogui.click(249, 1054)
    sleep(5)
    pyautogui.click(164, 63)
    pyautogui.write("computrabajo.com.ar")
    pyautogui.press('enter')
    sleep(10)
    #Busca si en la página de inicio está el nombre del usuario 
     #La ausencia del nombre de usuario indica que hay que loguearse
    if chequear("inicio.png", (1049, 89, 851, 70)):
        print("Logueado")
    else:   
        print("\nNo esta logueado. Logueando")
        pyautogui.click(1629, 200)
        sleep(10)
        if chequear("inicio.png", (1049, 89, 851, 70)):#Revisa si el intento de logueo fue exitoso
            print("\nLogueado")
        else:
            print("\nFalló intento de logueo")
            return 0
    

#Compara los resultados de la busqueda con una o mas palabras clave, devuelve una lista con las coordenadas de todos los anuncios encotrados. 
# O una lista vacia si no encuentra ninguna         
def buscar_anuncios(palabras, sector):
    posiciones=[]
    for palabra in palabras:
        try:
            anuncios=pyautogui.locateAllOnScreen(palabra, confidence=0.9, region=sector)
            for anuncio in anuncios:
                posiciones.append(pyautogui.center(anuncio))
        except:
            pass
    return posiciones
    









#Toma como argumentos el nombre de un archivo png y un sector de la pantalla. 
# Revisa si la imagen se encuentra en el sector de pantalla indicado. Devuelve True si está y False si no
def chequear(imagen, sector): 
    try:
        pyautogui.locateOnScreen(imagen, region=sector, confidence=0.9)
    except:
        return False
    else:
        return True

def busqueda_general(trabajo, lugar):
    pyautogui.click(960, 422)
    pyautogui.write(lugar)
    pyautogui.click(690, 417)
    pyautogui.write(trabajo)
    pyautogui.press('enter')
    sleep(10)


def preguntas():
#Esta función es llamada cuando el anuncio pide responder preguntas adicionales, la macro marcara el anuncio como favorito
    print("Llegamos aqui")
    foco=pyautogui.locateCenterOnScreen("preguntas.png", region=AREA_POSTULACIONES, confidence=0.9)
    pyautogui.click(foco) #hace foco en el area de postulaciones
    buscar=True
    while(buscar):
        try:
            volver=pyautogui.locateCenterOnScreen("volver.png", region=AREA_POSTULACIONES, confidence=0.9)
        except:
            pyautogui.press("pagedown")
            sleep(5)
        else:
            buscar=False
    pyautogui.click(volver)
    sleep(5)
    try:
        clickear=pyautogui.locateCenterOnScreen("favorito.png", region=AREA_POSTULACIONES, confidence=0.9)
        pyautogui.click(clickear)
    except:
        print("Me voy a volver Chango")
    sleep(5)


def postularse(anuncios):
    postulado_exitosamente=0
    ya_postulado=0
    responder_preguntas=0
    for encontrado in anuncios:
        pyautogui.click(encontrado)
        sleep(5)
        if not chequear("yaFavorito.png", AREA_POSTULACIONES):
            try:
                clickear=pyautogui.locateCenterOnScreen("postularme.png", region=AREA_POSTULACIONES, confidence=0.9)
                pyautogui.click(clickear)
                sleep(5)
                if chequear("preguntas.png", AREA_POSTULACIONES):
                    responder_preguntas+=1
                    preguntas()
                elif ("yaPostulado.png", AREA_POSTULACIONES):
                    ya_postulado+=1
                else:
                    postulado_exitosamente+=1
                
            except:
                print("Falló postulacion")
        else:
            print("Estaba guardado en favoritos")
    return (postulado_exitosamente, ya_postulado, responder_preguntas)




sleep(5)
entrar()
busqueda_general("", "capital federal")
palabras="operario.png", "deposito.png"
for _ in range(10):
    anuncios = buscar_anuncios(palabras, AREA_ANUNCIOS)
    print(f"Número de anuncios encontrados: {len (anuncios)}")
    stats = postularse(anuncios)
    print(f"{stats}")
    sleep(5)
    try:
        pasar_pagina=pyautogui.locateCenterOnScreen("siguiente.png", region=AREA_ANUNCIOS, confidence=0.9)
        pyautogui.click(pasar_pagina)
    except:
        pyautogui.click(572, 261)
        sleep(2)
        pyautogui.press("pagedown")
