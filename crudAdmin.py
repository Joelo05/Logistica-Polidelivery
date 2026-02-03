

import json
import os

ARCHIVO = "datos/centros.txt"
os.makedirs("datos", exist_ok=True)


def cargar_datos():
    if not os.path.exists(ARCHIVO):
        return {}, {}
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("centros", {}), data.get("rutas", {})


def guardar_datos(centros, rutas):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump({"centros": centros, "rutas": rutas}, f, indent=4)


def agregar_centro(centros):
    nombre = input("Nombre del centro: ")
    region = input("Región: ")
    centros[nombre] = region


def actualizar_centro(centros):
    nombre = input("Centro a actualizar: ")
    if nombre in centros:
        centros[nombre] = input("Nueva región: ")
    else:
        print("Centro no encontrado")


def eliminar_centro(centros, rutas):
    nombre = input("Centro a eliminar: ")
    centros.pop(nombre, None)
    rutas.pop(nombre, None)
    for r in rutas.values():
        r.pop(nombre, None)


def agregar_ruta(rutas):
    o = input("Origen: ")
    d = input("Destino: ")
    c = int(input("Costo: "))
    rutas.setdefault(o, {})[d] = c
    rutas.setdefault(d, {})[o] = c


def burbuja(lista):
    for i in range(len(lista)):
        for j in range(0, len(lista)-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista


def insercion(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i-1
        while j >= 0 and lista[j] > key:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = key
    return lista


def seleccion(lista):
    for i in range(len(lista)):
        min_i = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[min_i]:
                min_i = j
        lista[i], lista[min_i] = lista[min_i], lista[i]
    return lista


def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    mid = len(lista)//2
    izq = merge_sort(lista[:mid])
    der = merge_sort(lista[mid:])
    return merge(izq, der)


def merge(a, b):
    res = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            res.append(a[i]); i+=1
        else:
            res.append(b[j]); j+=1
    res.extend(a[i:]); res.extend(b[j:])
    return res


def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    menores = [x for x in lista[1:] if x <= pivote]
    mayores = [x for x in lista[1:] if x > pivote]
    return quick_sort(menores) + [pivote] + quick_sort(mayores)


def busqueda_lineal(lista, x):
    for i, v in enumerate(lista):
        if v == x:
            return i
    return -1


def busqueda_binaria(lista, x):
    ini, fin = 0, len(lista)-1
    while ini <= fin:
        mid = (ini + fin)//2
        if lista[mid] == x:
            return mid
        if lista[mid] < x:
            ini = mid + 1
        else:
            fin = mid - 1
    return -1


def busqueda_interpolacion(lista, x):
    low, high = 0, len(lista)-1
    while low <= high and x >= lista[low] and x <= lista[high]:
        pos = low + int(((float(high-low) / (lista[high]-lista[low])) * (x - lista[low])))
        if lista[pos] == x:
            return pos
        if lista[pos] < x:
            low = pos + 1
        else:
            high = pos - 1
    return -1


def menu_admin():
    centros, rutas = cargar_datos()

    while True:
        print("\n--- MENU ADMINISTRADOR ---")
        print("1. Agregar centro")
        print("2. Actualizar centro")
        print("3. Eliminar centro")
        print("4. Agregar ruta")
        print("5. Guardar cambios")
        print("6. Salir")

        op = input("Opción: ")

        if op == "1": agregar_centro(centros)
        elif op == "2": actualizar_centro(centros)
        elif op == "3": eliminar_centro(centros, rutas)
        elif op == "4": agregar_ruta(rutas)
        elif op == "5": guardar_datos(centros, rutas)
        elif op == "6": break

