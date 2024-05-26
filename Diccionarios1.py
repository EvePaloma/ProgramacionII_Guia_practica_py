'''
Contar letras: Escribe una función que reciba una cadena y devuelva un diccionario
con la frecuencia de cada letra en la cadena.
'''

def contar_letras(cadena):
    frecuencia = {}

    for letra in cadena:
        if letra.isalpha():
            letra = letra.lower()
            if letra in frecuencia:
                frecuencia[letra] += 1
            else:
                frecuencia[letra] = 1    

    return frecuencia

cadena = "Escribe una función que reciba una cadena y devuelva un diccionario"
resultado = contar_letras(cadena)
print(f"La frecuencia de cada letra es de: {resultado}")            