import requests
import sys

BASE_URL = "http://localhost:5000"

def registrar_usuario():
    print("\n=== Registro de Usuario ===")
    usuario = input("Usuario: ").strip()
    clave = input("Contraseña: ").strip()

    if not usuario or not clave:
        print("Usuario y contraseña no pueden estar vacíos")
        return

    payload = {"usuario": usuario, "contraseña": clave}
    try:
        r = requests.post(f"{BASE_URL}/registro", json=payload)
        if r.status_code == 201:
            print("OK", r.json().get("mensaje"))
        else:
            print("Error:", r.json().get("error"))
    except requests.exceptions.ConnectionError:
        print("o se pudo conectar con el servidor")

def iniciar_sesion():
    print("\n=== Inicio de Sesión ===")
    usuario = input("Usuario: ").strip()
    clave = input("Contraseña: ").strip()

    payload = {"usuario": usuario, "contraseña": clave}
    try:
        r = requests.post(f"{BASE_URL}/login", json=payload)
        if r.status_code == 200:
            print("OK", r.json().get("mensaje"))
            return True
        else:
            print("Error:", r.json().get("error"))
            return False
    except requests.exceptions.ConnectionError:
        print("No se pudo conectar con el servidor")
        return False

def ver_tareas():
    print("\n=== Tareas ===")
    try:
        r = requests.get(f"{BASE_URL}/tareas")
        if r.status_code == 200:
            print(r.text)
        else:
            print("Error:", r.status_code, r.text)
    except requests.exceptions.ConnectionError:
        print("No se pudo conectar con el servidor")

def menu():
    while True:
        print("\n============================")
        print(" Sistema de Gestión de Tareas ")
        print("============================")
        print("1) Registro")
        print("2) Inicio de sesión")
        print("3) Tareas")
        print("4) Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            if iniciar_sesion():
                print("Ahora podés ver las tareas en la opción 3.")
        elif opcion == "3":
            ver_tareas()
        elif opcion == "4":
            print("👋 Saliendo...")
            sys.exit()
        else:
            print("Opción inválida, intente nuevamente")

if __name__ == "__main__":
    menu()
