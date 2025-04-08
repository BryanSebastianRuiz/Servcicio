def main():
    print("== CrackMe Nivel 1 ==")
    clave = input("Introduce la contraseña: ")

    if clave == "cyber123":
        print("Flag encontrada: flag{cyber123}")
    else:
        print("Contraseña incorrecta.")

    input("\nPresiona Enter para salir...")  # Evita que se cierre de inmediato

main()
