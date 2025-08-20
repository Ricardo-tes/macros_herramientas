import pyautogui
import shelve
#from PIL import Image
from pynput.keyboard import Key, Listener

def on_press(key):
    if key ==Key.shift:
        return False
def esperar_enter():
#Detecta cuando se presiona la tecla shift sin necesidad de que el programa esté en foco. Ignorará cualquier otra tecla
    with Listener(on_press=on_press) as listener:
            listener.join()
#La funcion muestra una captura
# del area seleccionada. Se puede guardar la captura o descartarla. Si el area es correcta para el usuario la retorna, sino retorna None. 

def medir_zona():
# Permite delimitar una zona rectangular de la pantalla indicando dos esquinas, la superior izquierda y la inferior derecha. Retorna la región en formato diccionario
    zona={}
    print("Ubique el puntero del mouse en la esquina superior izquierda y oprima shift")
    esperar_enter()
    six, siy =pyautogui.position()
    print("Ubique el puntero del mouse en la esquina inferior derecha y oprima shift")
    esperar_enter()
    idx, idy =pyautogui.position()
    zona["ancho"] = abs(idx-six)
    zona["alto"] = abs(idy-siy)
    zona["x"]=six
    zona["y"]=siy
    return (zona)

    # 
    # nombre=input("\nSi quiere guardar la capura ingrese el nombre. De lo contrario presione enter ")
    # if nombre != "":
    #     nombre=nombre+".png"
    #     captura.save(nombre, "PNG")
    # confirma=input("\nEl area delimitada es la correcta? s/n Enter ")
    # if confirma.lower() =='s':

        
    #     return zona
    # else:
    #     return None

def tomar_punto():
#Toma coordenas xy de un punto de la pantalla y lo retorna en formato cordenada x, cordenada y
    print("\nPosicione el puntero donde quiera tomar la posicio y presione enter")
    with Listener(on_press=on_press) as listener: #Detecta cuando se presiona enter sin necesidad de que el programa esté en foco
        listener.join()
    return (pyautogui.position())


def guardar_zona():
    zona=medir_zona()
    tupla_zona= zona['x'], zona['y'], zona['ancho'], zona['alto']
    print(f"Zona medida= {tupla_zona}\n")
    mostrar=input("Quiere ver una imagen de la zona capturada? (s/n)")
    if mostrar.lower()=='s':
        captura = pyautogui.screenshot(region=tupla_zona)
        captura.show()


# punto = tomar_punto()
# if punto!= None:
#     etiqueta = input("\nIngrese un nombre para etiquetar el punto a guardar ")
#     with shelve.open('puntos', 'c') as puntos:
#         puntos[etiqueta]=punto

 
# zona = tomar_zona()
# if zona != None:
#     print(zona)
#     etiqueta=input("\nIngrese nombre para etiquetar la zona guardada ")
#     with shelve.open('zonas', 'c') as base_zona:
#         base_zona[etiqueta] = zona
    
guardar_zona()