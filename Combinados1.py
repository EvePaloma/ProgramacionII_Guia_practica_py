'''
Contar palabras en frases: Escribe una función que reciba una lista de frases y
devuelva un diccionario donde las claves son las palabras y los valores son las
frecuencias de esas palabras en todas las frases.
'''

def contar_palabras(lista_frases):
    frecuencia = {}

    for frase in lista_frases:
        palabras = frase.split()
        for palabra in palabras:
            palabra = palabra.strip(",;.-""'¿?¡!()/")
            if palabra in frecuencia:
                frecuencia[palabra] += 1
            else:
                frecuencia[palabra] = 1

    return frecuencia

lista_de_frases = ["Cuando cuentes cuentos, cuenta cuantos cuentos cuentas, porque si no cuentas cuantos cuentos cuentas, nunca sabrás cuantos cuentos sabes contar"]
frecuencia = contar_palabras(lista_de_frases)
print(f"El diccionario es:{frecuencia}") 


        