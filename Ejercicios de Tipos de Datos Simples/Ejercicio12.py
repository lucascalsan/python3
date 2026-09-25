#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene 
#un descuento del 60%. Escribir un programa que comience leyendo el número de 
#barras vendidas que no son del día. Después el programa debe mostrar el precio 
#habitual de una barra de pan, el descuento que se le hace por no ser fresca y el 
#coste final total.


barras = int(input("Introduce el número de barras del día vendidas: "))

precio_habitual = 3.49
descuento = (60/100)
precio_con_descuento = precio_habitual * (1 - descuento)

coste_total = barras * precio_con_descuento

print(f"Precio habitual de una barra: {precio_habitual:.2f} €")
print(f"Descuento por no ser fresca: {descuento * 100:.0f}%")
print(f"Coste total a pagar: {coste_total:.2f} €")



