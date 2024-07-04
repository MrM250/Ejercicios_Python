def guardar_usuarios(nombre, usuario, password):
    with open(nombre, "a") as archivo:
        archivo.write(f"Usuario: {usuario}\n Password: {password}\n")

def crear_usuario(database: str):
    nombre = f"{database}.txt"
    usuario = input("Introduce el nombre del nuevo usuario: ")
    password = input("Introduce su contraseña: ")
    
    guardar_usuarios(nombre, usuario, password)
    print("Base de datos de usuarios guardada.")

base_de_datos = input("Introduce el nombre de la base de datos: ")
crear_usuario(base_de_datos)
