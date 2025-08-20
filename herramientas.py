import pyautogui
import shelve
#from PIL import Image
from pynput.keyboard import Key, Listener

def on_press(key):
#Detecta cuando se presiona enter
    if key==Key.enter:
        return False


def tomar_zona():

# Permite delimitar una zona rectangular de la pantalla indicando dos esquinas, la superior izquierda y la inferior derecha. La funcion muestra una captura
# del area seleccionada. Se puede guardar la captura o descartarla. Si el area es correcta para el usuario la retorna, sino retorna None. 
#
    print("Ubique el puntero del mouse en la esquina superior izquierda y oprima enter")
    with Listener(on_press=on_press) as listener:
        listener.join()
    six, siy =pyautogui.position()
    print("Ubique el puntero del mouse en la esquina inferior derecha y oprima enter")
    with Listener(on_press=on_press) as listener:
        listener.join()
    idx, idy =pyautogui.position()
    ancho = abs(idx-six)
    alto = abs(idy-siy)
    zona = (six, siy, ancho, alto)
    captura = pyautogui.screenshot(region=zona)
    captura.show()
    nombre=input("\nSi quiere guardar la capura ingrese el nombre. De lo contrario presione enter ")
    if nombre != "":
        nombre=nombre+".png"
        captura.save(nombre, "PNG")
    confirma=input("\nEl area delimitada es la correcta? s/n Enter ")
    if confirma.lower() =='s':

        
        return zona
    else:
        return None

def tomar_punto():
#Toma coordenas xy de un punto de la pantalla
    input("\nPosicione el puntero donde quiera tomar la posicio y presione enter")
    punto = pyautogui.position()
    confirma = input(f"Coordenadas: \nX: {punto.x} \nY: {punto.y} \nGuardar punto? s/n Enter ")
    if confirma.lower()=='s':
        return (punto)
    else:
        return None





# punto = tomar_punto()
# if punto!= None:
#     etiqueta = input("\nIngrese un nombre para etiquetar el punto a guardar ")
#     with shelve.open('puntos', 'c') as puntos:
#         puntos[etiqueta]=punto

 
zona = tomar_zona()
if zona != None:
    print(zona)
    etiqueta=input("\nIngrese nombre para etiquetar la zona guardada ")
    with shelve.open('zonas', 'c') as base_zona:
        base_zona[etiqueta] = zona
    
