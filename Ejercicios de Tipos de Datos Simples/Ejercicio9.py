#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
#y el número de años, y muestre por pantalla el capital obtenido en la inversión.

cantidad = float(input("Cantidad a invertir: "))
interes = float(input("Interés anual (%): "))
años = int(input("Número de años: "))

capital = cantidad * (1 + interes / 100) ** años
print(f"El capital obtenido es: {capital:.2f}")
