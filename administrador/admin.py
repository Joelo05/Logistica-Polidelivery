

RUTA_CENTROS = "data/centros.txt"

def cargar_centros():
    centros = []
    try:
        with open(RUTA_CENTROS, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue

                partes = linea.split(",")
                if len(partes) != 4:
                    print("Línea inválida ignorada:", linea)
                    continue

                origen, destino, distancia, costo = partes

                centros.append({
                    "origen": origen,
                    "destino": destino,
                    "distancia": int(distancia),
                    "costo": int(costo)
                })
    except FileNotFoundError:
        pass

    return centros



def guardar_centros(centros):
    with open(RUTA_CENTROS, "w", encoding="utf-8") as f:
        for c in centros:
            f.write(f"{c['origen']},{c['destino']},{c['distancia']},{c['costo']}\n")



def agregar_centro(centros):
    print("\nAGREGAR CENTRO / RUTA")
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

    print("Centro agregado correctamente")


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
        if a[0][clave].lower() < b[0][clave].lower():
            resultado.append(a.pop(0))
        else:
            resultado.append(b.pop(0))
    return resultado + a + b


def listar_centros(centros):
    print("\n LISTA DE CENTROS (MERGE SORT)")
    ordenados = merge_sort(centros.copy(), "origen")

    for i, c in enumerate(ordenados, start=1):
        print(f"{i}. {c['origen']} → {c['destino']} | {c['distancia']} km | ${c['costo']}")



def buscar_centro_lineal(centros, origen):
    for c in centros:
        if c["origen"].lower() == origen.lower():
            return c
    return None



def actualizar_centro(centros):
    print("\n ACTUALIZAR CENTRO")
    origen = input("Ingrese el centro origen a actualizar: ")
    centro = buscar_centro_lineal(centros, origen)

    if centro:
        centro["destino"] = input("Nuevo destino: ")
        centro["distancia"] = int(input("Nueva distancia (km): "))
        centro["costo"] = int(input("Nuevo costo ($): "))
        print(" Centro actualizado correctamente")
    else:
        print(" Centro no encontrado")


def eliminar_centro(centros):
    print("\nELIMINAR CENTRO")
    origen = input("Centro origen a eliminar: ")

    for i, c in enumerate(centros):
        if c["origen"].lower() == origen.lower():
            centros.pop(i)
            print(" Centro eliminado")
            return

    print(" Centro no encontrado")


def menu_admin():
    centros = cargar_centros()

    while True:
        print("\n MENÚ ADMINISTRADOR - POLIDELIVERY")
        print("1. Agregar centro o ruta")
        print("2. Listar centros (Merge Sort)")
        print("3. Consultar centro (Búsqueda Lineal)")
        print("4. Actualizar centro")
        print("5. Eliminar centro")
        print("6. Guardar cambios")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_centro(centros)

        elif opcion == "2":
            listar_centros(centros)

        elif opcion == "3":
            origen = input("Centro origen a buscar: ")
            centro = buscar_centro_lineal(centros, origen)
            if centro:
                print(centro)
            else:
                print(" Centro no encontrado")

        elif opcion == "4":
            actualizar_centro(centros)

        elif opcion == "5":
            eliminar_centro(centros)

        elif opcion == "6":
            guardar_centros(centros)
            print(" Cambios guardados en centros.txt")

        elif opcion == "7":
            print(" Saliendo del menú administrador")
            break

        else:
            print(" Opción inválida")
