#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
#y el número de años, y muestre por pantalla el capital obtenido en la inversión cada
#año que dura la inversión.

cantidad = float(input("Introduce la cantidad a invertir: "))
interes_anual = float(input("Introduce el interés anual (en porcentaje): "))
años = int(input("Introduce el número de años: "))

interes_anual /= 100

for año in range(1, años + 1):
    capital = cantidad * (1 + interes_anual) ** año
    print(f"Año {año}: {capital:.2f}")