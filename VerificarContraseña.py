def validar_password(password):
    if len(password) < 12:
        return False
    elif not any([c.isdigit() for c in password]):
        return False
    elif not any([c.islower() for c in password]):
        return False
    elif not any([c.isupper() for c in password]):
        return False
    else:
        return True
    
contraseña = input("Intrduce una contraseña: ")

if validar_password(contraseña):
    print("La contraseña es valida.")
else:
    print("La contraseña NO es valida.")
