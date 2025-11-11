# 4. Heladería “Frosty” — Sabor y topping
# Sabores y precios:

# chocolate → $4.000
# vainilla → $3.500
# Opcional: topping cuesta $1.000.

# Si el usuario ingresa un sabor que no existe, mostrar "Sabor no disponible".
# Si el sabor es válido, preguntar si quiere topping y calcular total.

sabor_helado = input("Ingrese el sabor de helado (chocolate/vainilla): ").lower()

total = 0

if sabor_helado == "chocolate" or sabor_helado == "vainilla":
    topping = input("¿Desea agregar topping por $1.000? (s/n): ").lower()
    
    if sabor_helado == "chocolate":
        total += 4000  
    
    elif sabor_helado == "vainilla":
        total += 3500
    
    if topping == "s":
        total += 1000    
else:
    print("Sabor no disponible")
    
print("El total a pagar es: $", total)
    
