#Desarrolla un programa en Python que solicite al usuario que ingrese 
#una frase y luego cuente y muestre el número de palabras en esa frase.

frase = input("Ingrese una frase: ")
palabras = frase.split()
num_palabras = len(palabras)

print("El numero de palabras en la frase es de: ",num_palabras)

