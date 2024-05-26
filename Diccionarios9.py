'''
Actualizar diccionario: Escribe una función que tome un diccionario y una lista de
tuplas (clave, valor) y actualice el diccionario con esas tuplas.
'''
def actualizar_diccionario(diccionario,lista_tuplas):
    for clave,valor in lista_tuplas:
        diccionario[clave] = valor

    return diccionario

diccionario = {'a':10,'b':20,'c':30}
tuplas = [('d',40),('e',50),('f',60)]
resultado = actualizar_diccionario(diccionario,tuplas)
print(f"El diccionario actualizado es:{resultado}")
