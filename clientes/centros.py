from clientes.arbol import *
from usuarios.registro import *
import heapq

centros_seleccionados = []
nombre_cliente = None

def obtener_nombre(nombre):
    global nombre_cliente
    nombre_cliente = nombre

def seleccionar_centro(centros):
    nombre = input("Ingrese el nombre del centro: ").strip()

    centro_encontrado = busqueda_lineal(centros, nombre)

    if centro_encontrado:
        if nombre not in centros_seleccionados:
            centros_seleccionados.append(centro_encontrado["centro"])
            print("Centro agregado correctamente.")
        else:
            print("El centro ya fue seleccionado.")
    else:
        print("El centro no existe en el sistema.")

def mostrar_centros_seleccionados():
    if not centros_seleccionados:
        print("No hay centros seleccionados.")
    else:
        print("Centros seleccionados:")
        for i, centro in enumerate(centros_seleccionados, start=1):
            print(f"{i}. {centro}")

def eliminar_centro():
    nombre = input("Ingrese el centro a eliminar de la selección: ").strip()

    if nombre in centros_seleccionados:
        centros_seleccionados.remove(nombre)
        print("Centro eliminado de la selección.")
    else:
        print("El centro no está en la selección.")

def calcular_costo_total():
    if len(centros_seleccionados) < 2:
        print("Debe seleccionar al menos dos centros.")
        return 0

    costo_total = 0

    for i in range(len(centros_seleccionados) - 1):
        origen = centros_seleccionados[i]
        destino = centros_seleccionados[i + 1]

        costo, ruta = dijkstra(origen, destino)
        print(f"Ruta: {ruta} | Costo: {costo}")

        costo_total += costo

    print(f"\nCosto total del envío: {costo_total}")
    return costo_total

def guardar_ruta(costo_total):
    if nombre_cliente is not None:
        nombre_archivo = f"rutas-{nombre_cliente}.txt"

        with open(f"data/{nombre_archivo}", "w", encoding="UTF-8") as archivo:
            archivo.write(f"Cliente: {nombre_cliente}\n")
            archivo.write("Centros seleccionados:\n")

            for centro in centros_seleccionados:
                archivo.write(f"- {centro}\n")

            archivo.write(f"\nCosto total del envío: {costo_total}\n")

        print(f"Ruta guardada correctamente en {nombre_archivo}")
    else:
        print("nombre de cliente no conseguido") # sujeto a cambios

def burbuja_centros(centros):
    n = len(centros)
    for i in range(n):
        for j in range(0, n - i - 1):
            if centros[j]["centro"] > centros[j + 1]["centro"]:
                centros[j], centros[j + 1] = centros[j + 1], centros[j]

def mostrar_centros(centros):
    print("\nCentros de distribución:")
    for i, c in enumerate(centros, start=1):
        print(f"{i}. {c['centro']} ({c['region']} - {c['subregion']})")

def busqueda_lineal(centros, nombre):
    for c in centros:
        if c["centro"].lower() == nombre.lower():
            return c
    return None

grafo = cargar_grafo_desde_archivo("data/rutas.txt")

def agregar_ruta(origen, destino, costo):
    if origen not in grafo:
        grafo[origen] = []
    grafo[origen].append((destino, costo))


def dijkstra(inicio, fin):
    cola = [(0, inicio, [])]
    visitados = set()

    while cola:
        (c, nodo, path) = heapq.heappop(cola)
        if nodo not in visitados:
            visitados.add(nodo)
            path = path + [nodo]
            if nodo == fin:
                return c, path
            
            for (vecino, costo_ruta) in grafo.get(nodo, []):
                if vecino not in visitados:
                    heapq.heappush(cola, (c + costo_ruta, vecino, path))
    return 0, []

 
def bfs(inicio):
    visitados = []
    cola = [inicio]
    while cola:
        nodo = cola.pop(0)
        if nodo not in visitados:
            visitados.append(nodo)
            for (v, _) in grafo.get(nodo, []):
                cola.append(v)
    return visitados

def dfs(nodo, visitados=None):
    if visitados is None:
        visitados = []
    visitados.append(nodo)
    for (v, _) in grafo.get(nodo, []):
        if v not in visitados:
            dfs(v, visitados)
    return visitados

