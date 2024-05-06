#Ejercicio 6: Validación de Contraseña 
#Escribe un programa en Python que valide una contraseña ingresada por el usuario. La contraseña debe cumplir con los siguientes requisitos:
#Debe tener al menos 8 caracteres de longitud.
#Debe contener al menos una letra mayúscula, una letra minúscula, un número y un carácter especial (por ejemplo, !, @, #, $, %, etc.). 
#El programa debe informar al usuario si la contraseña es válida o no.


# verificar si la longitud de la contraseña es menor 8 
def validacion_contraseña(contraseña):
    if len (contraseña) < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
        return False
    
    #Inicializar una lista de requisitos con valores False para cada tipo de caracter
    requisitos = [False,False,False,False,False,False]
    
    #Recorrer cada caracter
    for char in contraseña:
        if char.isupper():
            requisitos[0] = True
        elif char in "Ñ":
            requisitos[1] = True    
        elif char.islower():
            requisitos[2] = True
        elif char in  "ñ":
            requisitos[3]    
        elif char.isdigit():
            requisitos[4] = True
        elif char in "!#$%&/()=?¡<>[]_-+°^}{":
            requisitos[5] = True

     #Imprimir requisitos para verificar
    #print("Requisitos: ", requisitos)
    
    #Verificar requisitos
    if not all(requisitos):
        print("La contraseña debe contener al menos una letra mayuscula, una letra minúscula, un número y un caracter especial.")
        return False
    
    return True

#Validar contraseña   
contraseña = input("Ingrese contraseña: ")

while not validacion_contraseña(contraseña):
    contraseña = input("Por favor, ingrese una contraseña válida: ")

    
print("La contraseña es válida.")

   
