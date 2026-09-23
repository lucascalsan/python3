peso = float(input("¿Cuál es tu peso en kg? "))
estatura = float(input("¿Cuál es tu estatura en metros? "))
imc = peso / estatura ** 2
#imc indice de masa corporal
print(f"Tu índice de masa corporal es {imc:.2f}")
# : --> Separa el nombre de la variable de las instrucciones de formato.
# .2f --> Indica que se desea mostrar el valor con dos decimales y en formato de punto flotante.
