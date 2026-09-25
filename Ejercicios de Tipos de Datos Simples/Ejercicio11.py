#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de 
#interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de 
#año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que 
#comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, 
#introducida por el usuario. Después el programa debe calcular y mostrar por pantalla 
#la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada 
#cantidad a dos decimales. 


cantidad = float(input("Introduce la cantidad: "))

ano1 = cantidad * (4 / 100)
ano2 = cantidad * (4 / 100) + ano1
ano3 = cantidad * (4 / 100) + ano2

print(f"Saldo tras el primer año: {ano1:.2f} €")
print(f"Saldo tras el segundo año: {ano2:.2f} €")
print(f"Saldo tras el tercer año: {ano3:.2f} €")
