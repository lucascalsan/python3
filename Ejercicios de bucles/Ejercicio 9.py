# Escribir un programa que almacene la cadena de caracteres contraseña en una 
# variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña 
# correcta.

contrasena = "1234"
while True:
    a = input("Introduce la contraseña: ")
    
    if a == contrasena:
        print("¡Contraseña correcta! Acceso concedido.")
        break  
    else:
        print("Contraseña incorrecta. Inténtalo de nuevo.")