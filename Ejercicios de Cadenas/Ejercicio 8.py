#Escribir un programa que pregunte por consola el precio de un producto en euros 
#con dos decimales y muestre por pantalla el número de euros y el número de 
#céntimos del precio introducido. 

precio = input("Introduce el precio del producto en euros (con dos decimales): ")
precio = float(precio)
euros = int(precio)
centimos = int(round((precio - euros) * 100))
print(f"El precio es de {euros} euros y {centimos} céntimos.")
