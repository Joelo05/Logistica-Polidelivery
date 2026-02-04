def cargar_centros():
    centros = []
    try:
        with open("centros.txt", "r") as f:
            for linea in f:
                o, d, dist, costo = linea.strip().split(",")
                centros.append({
                    "origen": o,
                    "destino": d,
                    "distancia": int(dist),
                    "costo": int(costo)
                })
    except FileNotFoundError:
        pass
    return centros


def guardar_centros(centros):
    with open("centros.txt", "w") as f:
        for c in centros:
            f.write(f"{c['origen']},{c['destino']},{c['distancia']},{c['costo']}\n")

def agregar_centro(centros):
    origen = input("Centro origen: ")
    destino = input("Centro destino: ")
    distancia = int(input("Distancia (km): "))
    costo = int(input("Costo ($): "))

    centros.append({
        "origen": origen,
        "destino": destino,
        "distancia": distancia,
        "costo": costo
    })
    print(" Centro agregado")

def merge_sort(lista, clave):
    if len(lista) <= 1:
        return lista

    medio = len(lista) // 2
    izq = merge_sort(lista[:medio], clave)
    der = merge_sort(lista[medio:], clave)

    return merge(izq, der, clave)


def merge(a, b, clave):
    resultado = []
    while a and b:
        if a[0][clave] < b[0][clave]:
            resultado.append(a.pop(0))
        else:
            resultado.append(b.pop(0))
    return resultado + a + b


def listar_centros(centros):
    ordenados = merge_sort(centros.copy(), "origen")
    print("\n LISTA DE CENTROS")
    for i, c in enumerate(ordenados):
        print(f"{i}. {c['origen']} → {c['destino']} | {c['distancia']} km | ${c['costo']}")

def buscar_centro_lineal(centros, nombre):
    for c in centros:
        if c["origen"].lower() == nombre.lower():
            return c
    return None

def actualizar_centro(centros):
    nombre = input("Ingrese centro origen a actualizar: ")
    centro = buscar_centro_lineal(centros, nombre)

    if centro:
        centro["destino"] = input("Nuevo destino: ")
        centro["distancia"] = int(input("Nueva distancia: "))
        centro["costo"] = int(input("Nuevo costo: "))
        print(" Centro actualizado")
    else:
        print(" Centro no encontrado")

def eliminar_centro(centros):
    nombre = input("Centro origen a eliminar: ")
    for i, c in enumerate(centros):
        if c["origen"].lower() == nombre.lower():
            centros.pop(i)
            print("🗑️ Centro eliminado")
            return
    print(" Centro no encontrado")

def menu_admin():
    centros = cargar_centros()

    while True:
        print("\n MENÚ ADMINISTRADOR")
        print("1. Agregar centro o ruta")
        print("2. Listar centros (Merge Sort)")
        print("3. Consultar centro (Búsqueda Lineal)")
        print("4. Actualizar centro")
        print("5. Eliminar centro")
        print("6. Guardar cambios")
        print("7. Salir")

        op = input("Opción: ")

        if op == "1":
            agregar_centro(centros)

        elif op == "2":
            listar_centros(centros)

        elif op == "3":
            nombre = input("Centro origen: ")
            c = buscar_centro_lineal(centros, nombre)
            print(c if c else " No encontrado")

        elif op == "4":
            actualizar_centro(centros)

        elif op == "5":
            eliminar_centro(centros)

        elif op == "6":
            guardar_centros(centros)
            print(" Cambios guardados")

        elif op == "7":
            break

menu_admin()        