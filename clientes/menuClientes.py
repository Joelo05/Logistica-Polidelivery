from clientes.arbol import * 
from clientes.centros import * 

def menu_cliente():
    print("\n===== MENÚ CLIENTE =====")
    print("1. Ver mapa de centros conectados")
    print("2. Consultar la ruta óptima entre dos centros y su costo")
    print("3. Explorar centros organizados jerárquicamente por regiones")
    print("4. Seleccionar centros de distribución para un envío")
    print("5. Listar centros seleccionados y mostrar costo total")
    print("6. Aplicar algoritmo de ordenamiento a los centros")
    print("7. Actualizar selección de centros")
    print("8. Eliminar centros seleccionados")
    print("9. Guardar la selección en archivo (rutas-nombre-del-cliente.txt)")
    print("10. Salir")
    return input("Seleccione una opción: ")

def ejecutar_menu_cliente(nombre_cliente, dijkstra_func):
    centros = leer_centros_desde_archivo()
    arbol = construir_arbol_regiones(centros)

    while True:
        opcion = menu_cliente()

        if opcion == "1":
            # Ver mapa de centros conectados
            print("\nMapa de centros (estructura jerárquica):")
            mostrar_arbol(arbol)

        elif opcion == "2":
            # Consultar ruta óptima entre dos centros
            origen = input("Centro origen: ").strip()
            destino = input("Centro destino: ").strip()

            costo, ruta = dijkstra_func(origen, destino)
            print(f"Ruta óptima: {ruta}")
            print(f"Costo total: {costo}")

        elif opcion == "3":
            # Explorar centros por regiones
            print("\nCentros organizados por regiones:")
            mostrar_arbol(arbol)

        elif opcion == "4":
            # Seleccionar centros para envío
            seleccionar_centro(centros)

        elif opcion == "5":
            # Listar centros seleccionados y costo total
            mostrar_centros_seleccionados()
            calcular_costo_total(dijkstra_func)

        elif opcion == "6":
            # Aplicar algoritmo de ordenamiento
            burbuja_centros(centros)
            print("Centros ordenados alfabéticamente.")

        elif opcion == "7":
            # Actualizar selección de centros
            print("Selección actual:")
            mostrar_centros_seleccionados()
            seleccionar_centro(centros)

        elif opcion == "8":
            # Eliminar centros seleccionados
            eliminar_centro()

        elif opcion == "9":
            # Guardar la selección en archivo
            costo_total = calcular_costo_total(dijkstra_func)
            guardar_ruta(nombre_cliente, costo_total)

        elif opcion == "10":
            # Salir
            print("Saliendo del sistema del cliente...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")
