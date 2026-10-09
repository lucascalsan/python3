#Escribir un programa que almacene la cadena de caracteres contraseña en una
#variable, pregunte al usuario por la contraseña e imprima por pantalla si la
#contraseña introducida por el usuario coincide con la guardada en la variable sin
#tener en cuenta mayúsculas y minúsculas

print("Introduce la contraseña: ")
contraseña = "1234"
input_contraseña = input()

if input_contraseña == contraseña:
    print("La contraseña es correcta.")
else:
    print("La contraseña es incorrecta.")
