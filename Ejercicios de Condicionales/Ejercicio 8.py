puntuacion = float(input("Introduce la puntuación: "))

if puntuacion == 0.0:
    print("Nivel: Inaceptable")
    print("Dinero:", puntuacion * 2400)
elif puntuacion == 0.4:
    print("Nivel: Aceptable")
    print("Dinero:", puntuacion * 2400)
elif puntuacion >= 0.6:
    print("Nivel: Meritorio")
    print("Dinero:", puntuacion * 2400)
else:
    print("Puntuación no válida")