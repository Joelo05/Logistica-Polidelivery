from usuarios.registro import registrar_usuario
from usuarios.login import login
from clientes.menuClientes import ejecutar_menu_cliente

def menu():
    while True:
        print("\n--- POLIDELIVERY ---")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()

        elif opcion == "2":
            rol = login()
            if rol == "admin":
                print("Menú administrador")
            elif rol == "cliente":
                print("Menú cliente")
                ejecutar_menu_cliente()
        elif opcion == "3":
            print(" Saliendo del sistema")
            break

        else:
            print("Opción inválida")


menu()
