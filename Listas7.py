'''
7. Invertir lista: Escribe una función que tome una lista y devuelva una nueva lista con los
elementos en orden inverso.
'''

def invertir_lista(lista):
    return lista[::-1]

num = [10,20,30,40,50]
resultado = invertir_lista(num)
print(f"Elementos en orden inverso: {resultado}")
'''
palabras = ["hola, mundo"]
resultado = invertir_lista(palabras)
print(f"Elementos en orden inverso: {resultado}")
'''
