def leer_centros_desde_archivo():
    centros = []

    try:
        with open("data/centros.txt", "r") as archivo:
            for linea in archivo:
                centro, region, subregion = linea.strip().split(",")
                centros.append({
                    "centro": centro,
                    "region": region,
                    "subregion": subregion
                })

        return centros
    except FileNotFoundError:
        print("Archivo no encontrado")

def construir_arbol_regiones(centros):
    arbol = {"Ecuador": {}}

    for c in centros:
        region = c["region"]
        subregion = c["subregion"]
        centro = c["centro"]

        if region not in arbol["Ecuador"]:
            arbol["Ecuador"][region] = {}

        if subregion not in arbol["Ecuador"][region]:
            arbol["Ecuador"][region][subregion] = []

        arbol["Ecuador"][region][subregion].append(centro)

    return arbol

def mostrar_arbol(arbol, nivel=0):
    for clave, valor in arbol.items():
        print("  " * nivel + f"- {clave}")
        if isinstance(valor, dict):
            mostrar_arbol(valor, nivel + 1)
        elif isinstance(valor, list):
            for item in valor:
                print("  " * (nivel + 1) + f"- {item}")

def cargar_grafo_desde_archivo(nombre_archivo):
    grafo = {}

    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            origen, destino, costo = linea.strip().split(",")
            costo = int(costo)

            if origen not in grafo:
                grafo[origen] = []
            if destino not in grafo:
                grafo[destino] = []

            # Grafo no dirigido (bidireccional)
            grafo[origen].append((destino, costo))
            grafo[destino].append((origen, costo))

    return grafo
