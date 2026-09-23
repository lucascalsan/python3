#Escribir un programa que lea un entero positivo, , introducido por el usuario y
#después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La
#suma de los primeros enteros positivos puede ser calculada de la siguiente forma:
n = int(input("Introduce un numero entero positivo: "))
suma = n * (n + 1) // 2
print(f"La suma de los enteros desde 1 hasta {n} es {suma}.")