#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
#Los ingredientes para cada tipo de pizza aparecen a continuación.
#● Ingredientes vegetarianos: Pimiento y tofu.
#● Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y
#en función de su respuesta le muestre un menú con los ingredientes disponibles
#para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el
#tomate que están en todas las pizzas. Al final se debe mostrar por pantalla si la
#pizza elegida es vegetariana o no y todos los ingredientes que lleva.

vegano = input("¿Quieres pizza vegetariana? (sí/no): ").lower()

if vegano == "si":
    tipo = "Vegetariana"
    ingrediente = input("Elige ingrediente (1- Pimiento, 2- Tofu): ")
    extra = "Pimiento" if ingrediente == "1" else "Tofu"
else:
    tipo = "No vegetariana"
    ingrediente = input("Elige ingrediente (1- Peperoni, 2- Jamón, 3- Salmón): ")
    if ingrediente == "1": extra = "Peperoni"
    elif ingrediente == "2": extra = "Jamón"
    else: extra = "Salmón"

print(f"\nPizza {tipo} con Mozzarella, Tomate y {extra}.")
