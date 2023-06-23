import hashlib


def convertir_password(password):
    if len(password) < 6 or len(password) > 12:
        return "La contraseña debe tener entre 6 y 12 caracteres."

    # Aplicar hash MD5 a la contraseña
    hashed_password = hashlib.md5(password.encode()).hexdigest()

    # Rellenar con ceros a la izquierda para obtener una cadena de 32 caracteres
    hashed_password = hashed_password.zfill(32)
    print(hashed_password)
    return hashed_password

convertir_password("miClave")