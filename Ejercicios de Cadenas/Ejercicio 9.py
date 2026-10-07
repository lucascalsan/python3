#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato 
#dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa 
#anterior para que también funcione cuando el día o el mes se introduzcan con un 
#solo carácter.
fecha = input("Introduce tu fecha de nacimiento en formato dd/mm/aaaa: ")
dia, mes, año = fecha.split("/")
print(f"Has nacido el día {dia}, el mes {mes} y el año {año}.")
