cadastros = {
    "Kevin": 11248992270
}
while True:
    loginUsuario = input("Coloca tu usuario: ")
    loginCpf = input("Coloca tu CPF: ")

    if loginUsuario in cadastros and loginCpf == str(cadastros[loginUsuario]):
        print(f"Bienvenido {loginUsuario}")
    else :
        opcion = input("Usuario o CPF incorrectos,  (1):quieres volverlo a intentar, (2):quiere hacer un nuevo login? (1 o 2) : ")
        if opcion == 1:
            print("Intentalo de nuevo")
        elif opcion == 2:
            loginUsuario = input("Coloca tu usuario: ")
            loginCpf = input("Coloca tu CPF: ")
            cadastros[loginUsuario] = loginCpf
            print(f"Bienvenido {loginUsuario}")
        else :
            print("Campo llenado con error, intentalo de nuevo")