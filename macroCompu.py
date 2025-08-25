import pyautogui
from time import sleep
# Este programa es una macro que abre el navegador...



def iniciar():
#Entra a la página computrabajo, comprueba que esté logueado y si no lo está se loguea    
    nombre_pagina = "computrabajo.com.ar"
    browser = (203, 1060)
    barra_de_navegacion = (162, 61)
    nombre_de_usuario = "marcadores/usuario.png" 
    sector_de_usuario = (1225, 94, 334, 61)
    loguearse = (1629, 200)
    pyautogui.click(browser) #Abre el browser
    sleep(5)
    pyautogui.click(barra_de_navegacion) #Hace click en la barra de navegacion
    pyautogui.write(nombre_pagina) #Escribe la direccion de la página
    pyautogui.press('enter')
    sleep(10)
    if chequear(nombre_de_usuario, sector_de_usuario): #Busca si en la página de inicio está el nombre del usuario, si no está hay que loguearse
        print("Logueado")
    else:   
        print("\nNo esta logueado. Logueando")
        pyautogui.click(loguearse) #Hace click en el acceso rapido para loguearse con el mail
        sleep(10)
        if chequear(nombre_de_usuario, sector_de_usuario):#Revisa si el intento de logueo fue exitoso
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
            anuncios=pyautogui.locateAllOnScreen(palabra, region=sector)
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


def preguntas(sector_postulaciones):
#Esta función es llamada cuando el anuncio pide responder preguntas adicionales, la macro marcara el anuncio como favorito
    print("Llegamos aqui")
    foco=pyautogui.locateCenterOnScreen("marcadores/preguntas.png", region=sector_postulaciones, confidence=0.9)
    pyautogui.click(foco) #hace foco en el area de postulaciones
    buscar=True
    while(buscar):
        try:
            volver=pyautogui.locateCenterOnScreen("marcadores/volver.png", region=sector_postulaciones, confidence=0.9)
        except:
            pyautogui.press("pagedown")
            sleep(5)
        else:
            buscar=False
    pyautogui.click(volver)
    sleep(5)
    try:
        clickear=pyautogui.locateCenterOnScreen("marcadores/favorito.png", region=sector_postulaciones, confidence=0.9)
        pyautogui.click(clickear)
    except:
        print("Me voy a volver Chango")
    sleep(5)


def postularse(anuncios, sector_postulaciones):
    postulado_exitosamente=0
    ya_postulado=0
    responder_preguntas=0
    for encontrado in anuncios:
        pyautogui.click(encontrado)
        sleep(5)
        if not chequear("marcadores/ya_favorito.png", sector_postulaciones):
            try:
                clickear=pyautogui.locateCenterOnScreen("marcadores/postularme.png", region=sector_postulaciones, confidence=0.9)
                pyautogui.click(clickear)
                sleep(5)
                if chequear("marcadores/preguntas.png", sector_postulaciones):
                    responder_preguntas+=1
                    preguntas(sector_postulaciones)
                elif ("marcadores/ya_postulado.png", sector_postulaciones):
                    ya_postulado+=1
                else:
                    postulado_exitosamente+=1
                
            except:
                print("Falló postulacion")
        else:
            print("Estaba guardado en favoritos")
    return (postulado_exitosamente, ya_postulado, responder_preguntas)



def main():
    sector_postulaciones = (865, 241, 822, 813)
    sector_anuncios = (327, 140, 547, 919)
    trabajo=""
    lugar="capital federal"
    sleep(5)
    iniciar()
    busqueda_general(trabajo, lugar)
    palabras=["palabras_clave/operario.png", "palabras_clave/deposito.png"]
    for _ in range(10):
        anuncios = buscar_anuncios(palabras, sector_anuncios)
        print(f"Número de anuncios encontrados: {len (anuncios)}")
        stats = postularse(anuncios, sector_postulaciones)
        print(f"{stats}")
        sleep(5)
        try:
            pasar_pagina=pyautogui.locateCenterOnScreen("marcadores/siguiente.png", region=sector_anuncios, confidence=0.9)
            pyautogui.click(pasar_pagina)
        except:
            pyautogui.click(572, 261)
            sleep(2)
            pyautogui.press("pagedown")

main()