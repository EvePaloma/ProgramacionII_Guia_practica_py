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
    requisitos = [False,False,False,False]
    
    #Recorrer cada caracter
    for char in contraseña:
        if char in "abcdefghijklmnñopqrstuvwxyz":
            requisitos[0] = True
        elif char in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ":
            requisitos[1] = True    
        elif char.isdigit():
            requisitos[2] = True
        elif char in "!#$%&/()=?¡<>[]_-+°^}*{":
            requisitos[3] = True
        else:
            return False    

     #Imprimir requisitos para verificar
    #print("Requisitos: ", requisitos)
    
    #Verificar requisitos
    if not all(requisitos):
        print("La contraseña debe contener al menos una letra mayuscula, una letra minúscula, un número y un caracter especial.")
        return False
    
    return True

    #Validar contraseña   
while True:
    contraseña = input("Ingrese contraseña: ")
    if validacion_contraseña(contraseña):
        print("La contraseña es válida.")
        break
    else:
        print("Por favor, ingrese una contraseña válida.")

    


   
