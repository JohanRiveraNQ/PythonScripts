
from flask import request, abort
import hashlib
import hmac

# Define tu nueva clave secreta aquí
SECRET_KEY = b"1234567890"

def generar_hmac(contenido):
    # Genera el HMAC utilizando la clave secreta
    hmac_calculado = hmac.new(SECRET_KEY, contenido, hashlib.sha256).hexdigest()
    return hmac_calculado

if __name__ == "__main__":
    # Ejemplo de cómo utilizar la función generar_hmac
    contenido_ejemplo = b"Ejemplo de contenido"
    hmac_generado = generar_hmac(contenido_ejemplo)
    print("HMAC generado:", hmac_generado)