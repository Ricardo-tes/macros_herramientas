import pyautogui
import csv
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
    captura = pyautogui.screenshot(region=tupla_zona)
    accion=input(f"Quiere ver una imagen de la zona capturada? (s/n)\n")
    if accion.lower()=='s':
        captura.show()
    print(f"Zona medida= {tupla_zona}\n Resolucion: {zona['resolucion']}")
    accion = input(f"Quiere guardar las coordenadas de la zona marcada? s/n \n")
    if accion.lower()=='s':
        guardar(zona)
 
def guardar_punto():
    punto = medir_punto()
    print(f"El punto medido es ({punto['x']}, {punto['y']})\n Resolucion: {punto['resolucion']}\n")
    accion=input(f"Quiere guardar el punto? s/n\n")
    if accion.lower()=='s':
        guardar(punto)

def guardar_captura():
    zona=medir_zona()
    tupla_zona= zona['x'], zona['y'], zona['ancho'], zona['alto'] 
    captura = pyautogui.screenshot(region=tupla_zona)
    captura.show()
    nombre=input(f"Si quiere guardar la capura ingrese el nombre, de lo contrario presione enter ")
    if nombre != "":
         nombre=nombre+".png"
         captura.save(nombre, "PNG")


def main():
    menu=[guardar_punto, guardar_zona, guardar_captura]
    elegir=input(f"\n1 Guardar punto\n2 Guardar zona\n3 Guardar captura\nCaulquier otro caracter para salir\n")
    if elegir in "123":
        menu[int(elegir)-1]()

if __name__=="__main__":
    main()