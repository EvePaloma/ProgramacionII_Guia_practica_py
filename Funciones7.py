'''
Ejercicio 7
Contar letras: Crea una función que tome una cadena como entrada y devuelva un
diccionario con el recuento de cada letra en la cadena.
'''

def contar_letras(cadena):
    contar = {}

    for letra in cadena:
        if letra in contar:
            contar[letra] += 1

        else:
            contar[letra] = 1

    return contar

cadena = "programacion"
resultado = contar_letras(cadena)
print(resultado)        
