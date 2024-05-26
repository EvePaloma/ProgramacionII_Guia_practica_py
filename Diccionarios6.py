'''
Intercambiar valores: Crea una función que tome un diccionario y dos claves, e
intercambie los valores de esas dos claves en el diccionario.
'''

def intercambiar_valores(diccionario,clave1,clave2):

    if clave1 in diccionario and clave2 in diccionario:
        diccionario[clave1], diccionario[clave2] = diccionario[clave2], diccionario[clave1]

    return diccionario

diccionario = {'a':2,'b':4}
clave_1 = "a"
clave_2 = "b"
valores_intercambiados = intercambiar_valores(diccionario,clave_1,clave_2)
print(f"Los valores intercambiados de esas claves son: {valores_intercambiados}") 

