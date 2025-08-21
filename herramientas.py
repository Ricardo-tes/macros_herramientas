import pyautogui
import csv
#from PIL import Image
from pynput.keyboard import Key, Listener

def on_press(key):
    if key ==Key.shift_l:
        return False
def esperar_shift():
#Detecta cuando se presiona la tecla shift izquierda sin necesidad de que el programa esté en foco. Ignorará cualquier otra tecla
    with Listener(on_press=on_press) as listener:
            listener.join()
 
def medir_resolucion():
#Lee la resolucion de la pantalla y devuelve un string de formato anchoXalto
    ancho, alto = pyautogui.size()
    return (str(ancho)+'X'+str(alto))

def medir_zona():
# Permite delimitar una zona rectangular de la pantalla indicando dos esquinas, la superior izquierda y la inferior derecha. Retorna la región en formato diccionario
    zona={}
    print("Ubique el puntero del mouse en la esquina superior izquierda y oprima shift izquierdo")
    esperar_shift()
    six, siy =pyautogui.position()
    print("Ubique el puntero del mouse en la esquina inferior derecha y oprima shift izquierdo")
    esperar_shift()
    idx, idy =pyautogui.position()
    zona["ancho"] = abs(idx-six)
    zona["alto"] = abs(idy-siy)
    zona["x"]=six
    zona["y"]=siy
    zona["resolucion"]=medir_resolucion()
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

def medir_punto():
#Toma coordenas xy de un punto de la pantalla y lo retorna en formato cordenada x, cordenada y
    punto={}
    print("\nPosicione el puntero donde quiera tomar la posicio y presione shif izquierdo")
    esperar_shift()
    punto["x"], punto["y"] = pyautogui.position()
    punto["resolucion"]=medir_resolucion()
    return (punto)

def guardar(cordenadas):
#Almacena coordenadas, tanto zonas como puntos en un archivo csv
    fila={}
    nombre_archivo = "datos.csv"
    nombre=input(f"Ingrese un nombre para guardar las coordenadas\n")
    descripcion=input(f"Ingrese una descripcion. Opcional\n")
    fila["nombre"]=nombre
    fila["descripcion"]=descripcion
    fila["x"]=cordenadas["x"]
    fila["y"]=cordenadas["y"]
    fila["resolucion"]=cordenadas["resolucion"]
    if len(cordenadas)==5:
        fila["ancho"]=cordenadas["ancho"]
        fila["alto"]=cordenadas["alto"]
    else:
        fila["ancho"]=""
        fila["alto"]=""
    columnas=["nombre", "descripcion", "x", "y", "ancho", "alto", "resolucion"]
    with open (nombre_archivo, 'a') as archivo:
        csv_writer=csv.DictWriter(archivo, fieldnames=columnas)
        if archivo.tell()==0:
            csv_writer.writeheader()
        csv_writer.writerow(fila)

def guardar_zona():
    zona=medir_zona()
    tupla_zona= zona['x'], zona['y'], zona['ancho'], zona['alto']
    accion=input(f"Quiere ver una imagen de la zona capturada? (s/n)\n")
    if accion.lower()=='s':
        captura = pyautogui.screenshot(region=tupla_zona)
        captura.show()
    print(f"Zona medida= {tupla_zona}\n")
    accion = input(f"Quiere guardar las coordenadas de la zona marcada? s/n \n")
    if accion.lower()=='s':
        guardar(zona)
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
    
def guardar_punto():
    punto = medir_punto()
    print(f"El punto medido es ({punto['x']}, {punto['y']})\n")
    accion=input(f"Quiere guardar el punto? s/n\n")
    if accion.lower()=='s':
        guardar(punto)

guardar_punto()
guardar_zona()