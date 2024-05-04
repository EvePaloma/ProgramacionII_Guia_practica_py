#Ejercicio 8: Generador de Contraseñas Aleatorias 
#Escribe un programa en Python que genere una contraseña aleatoria para el usuario. 
#La contraseña debe tener una longitud de al menos 12 caracteres y debe contener 
#una combinación de letras (mayúsculas y minúsculas), números y caracteres especiales.
# El programa debe mostrar la contraseña generada al usuario.


import string
import random

def generar_contraseña(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ""
    for i in range(longitud):
        contraseña += random.choice(caracteres)
    return contraseña

contraseña_generada = generar_contraseña()
print("Contraseña generada: ", contraseña_generada)    