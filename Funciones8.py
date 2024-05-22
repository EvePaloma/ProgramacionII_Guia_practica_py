'''
Ejercicio 8
Palíndromo: Escribe una función que determine si una palabra o frase es un palíndromo (se
lee igual de adelante hacia atrás que de atrás hacia adelante), ignorando espacios y signos
de puntuación.
'''

def palindromo(cadena):

    cadena_limpia = "".join(l for l in cadena if l.isalnum()).lower()

    return cadena_limpia == cadena_limpia[::-1]

frase = "yo hago yoga hoy"
resultado = palindromo(frase)
print(resultado)

frase_con_num = "78987"
resultado = palindromo(frase_con_num)
print(resultado)