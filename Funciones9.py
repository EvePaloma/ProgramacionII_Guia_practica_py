'''
Ejercicio 9
Ordenar lista de cadenas: Escribe una función que tome una lista de cadenas y devuelva una
lista ordenada alfabéticamente de esas cadenas, ignorando mayúsculas y minúsculas.
'''

def ordenar_lista_cadena(lista):
    #Ordena la lista usando sorted() con str.lower como clave para ignorar mayúsculas y minúsculas
    return sorted(lista, key=str.lower)

lista_de_cadenas = ["GitHub", "programacion", "funciones", "Documentos"]
resultado = ordenar_lista_cadena(lista_de_cadenas)
print(resultado)