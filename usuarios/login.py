RUTA_USUARIOS = "data/usuarios.txt"


def login():
    correo = input("Correo: ")
    password = input("Contraseña: ")

    try:
        with open(RUTA_USUARIOS, "r") as f:
            for linea in f:
                datos = linea.strip().split(";")
                if datos[3] == correo and datos[4] == password:
                    print("Login exitoso")
                    return datos[5]  # rol
    except FileNotFoundError:
        pass

    print("Credenciales incorrectas")
    return None
