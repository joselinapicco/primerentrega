data = {}

def login():
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    if nombre_usuario in data:
        if data[nombre_usuario] == password:
            print("¡Bienvenido!")
        else:
            print("Contraseña incorrecta. Inténtelo nuevamente.")
    else:
        print("El usuario no existe.")
        
def mostrar_usuarios():
    if not data:
        print("No hay usuarios registrados.")
    else:
        print("Usuarios registrados:")
        for user in data:
            print(f"- {user}")

def registrar_usuario():
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    if nombre_usuario in data:
        print("El nombre de usuario ya existe. Inténtelo de nuevo.")
    password = input("Ingrese su contraseña: ")
    confirm_password = input("Confirme su contraseña: ")
    if password != confirm_password:
        print("Las contraseñas no coinciden. Inténtelo de nuevo.")
        return
    else:
        data[nombre_usuario] = password
        print("Usuario registrado con éxito")
    
while True:
    print("----- MENÚ -----")
    print("1. Crear un nuevo usuario")
    print("2. Ingresar")
    print("3. Mostrar usuarios registrados")
    print("4. Salir")
    
    opcion = input("Elija una opción para comenzar: ")
    
    if opcion == "1":
        registrar_usuario()
        input("Presione Enter para volver al menú...")
    elif opcion == "2":
        login()
        input("Presione Enter para volver al menú...")
    elif opcion == "3":
        mostrar_usuarios()
        input("Presione Enter para volver al menú...")
    elif opcion == "4":
        print("¡Adiós!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
        input("Presione Enter para volver al menú...")    
        

