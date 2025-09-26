from werkzeug.security import generate_password_hash, check_password_hash

def hash_clave(clave):
    """
    hashea una contraseña usando werkzeug.security
    """
    return generate_password_hash(clave)

def verificar_clave(clave_hash, clave_ingresada):
    """
    verifica si la contraseña ingresada coincide con el hash almacenado
    """
    return check_password_hash(clave_hash, clave_ingresada)