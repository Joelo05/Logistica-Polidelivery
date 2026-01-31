def validar_edad(edad):
    return edad >= 18


def validar_correo(correo):
    return (
        correo.count("@") == 1
        and correo.endswith("@gmail.com")
        and "." in correo.split("@")[0]
    )


def validar_contrasena(password):
    tiene_mayus = False
    tiene_minus = False
    tiene_num = False

    for c in password:
        if c.isupper():
            tiene_mayus = True
        elif c.islower():
            tiene_minus = True
        elif c.isdigit():
            tiene_num = True

    return tiene_mayus and tiene_minus and tiene_num and len(password) >= 8
