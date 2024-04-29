#Desarrolla un programa en Python que convierta una cantidad de dinero 
#de dólares estadounidenses a euros. El programa debe solicitar al usuario 
#que ingrese la cantidad en dólares y luego mostrar la cantidad equivalente en euros, 
#utilizando un tipo de cambio fijo.


tipo_cambio = 0.93

cantidad_dolares = float(input("Ingrese la cantidad de dolares: "))
cantidad_euros = cantidad_dolares * tipo_cambio

print("La cantidad equivalente en euros es de: ", cantidad_euros)