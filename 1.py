def crear_perfil_usuario(nombre, email, rol):
    
    if "@" not in email:
        return "Error: el email debe contener un símbolo '@'."
    
    perfil = {
        "nombre": nombre,
        "email": email,
        "rol": rol
    }
    
    return perfil
