#Escribir un programa que pida al usuario dos números y muestre por pantalla su 
#división. Si el divisor es cero el programa debe mostrar un error. 

dividendo = float(input("Introduce el dividendo: "))
divisor = float(input("Introduce el divisor: "))

if divisor == 0:
    print("Error: El divisor no puede ser cero.")
else:
    resultado = dividendo / divisor
    print(f"El resultado de la división es: {resultado}")
