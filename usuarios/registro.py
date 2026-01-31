from usuarios.validaciones import (
    validar_edad,
    validar_correo,
    validar_contrasena
)

RUTA_USUARIOS = "data/usuarios.txt"


def correo_existe(correo):
    try:
        with open(RUTA_USUARIOS, "r") as f:
            for linea in f:
                datos = linea.strip().split(";")
                if datos[3] == correo:
                    return True
    except FileNotFoundError:
        pass
    return False


def registrar_usuario():
    nombre = input("Nombre y apellido: ")
    cedula = input("Cédula: ")
    edad = int(input("Edad: "))
    correo = input("Correo: ")
    password = input("Contraseña: ")

    if not validar_edad(edad):
        print(" Debe ser mayor de edad")
        return

    if not validar_correo(correo):
        print(" Correo inválido")
        return

    if not validar_contrasena(password):
        print(" Contraseña insegura")
        return

    if correo_existe(correo):
        print("El correo ya está registrado")
        return

    with open(RUTA_USUARIOS, "a") as f:
        f.write(f"{nombre};{cedula};{edad};{correo};{password};cliente\n")

    print(" Usuario registrado con éxito")
