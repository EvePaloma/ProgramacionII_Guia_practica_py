'''
Ejercicio 1
Crea un función “ConvertirEspaciado”, que reciba como parámetro un texto y devuelve una
cadena con un espacio adicional tras cada letra. Por ejemplo, “Hola, tú” devolverá “H o l a , t
ú “. Crea un programa principal donde se use dicha función luego del ingreso del usuario.
'''

def convertir_espaciado():
    texto = input("Ingrese un texto: ")
    letra = " ".join(texto)

    return letra

texto_espaciado = convertir_espaciado()
print(texto_espaciado)




    