# 9. Supermercado “AhorroMax” — Descuentos y envío
# Cada producto cuesta $2.000.

# Reglas:

# 30 unidades → 15% descuento

# 10 unidades → 5% descuento

# Si el total después del descuento es < $50.000 → agregar $5.000 de envío
# Calcular total final.

precio = 2000
cantidad = int(input("Ingrese la cantidad de productos que desea comprar: "))
total = 0.0

if cantidad >= 10:
    
    if cantidad >= 30:
        descuento = 0.15
    else:
        descuento = 0.05
    
total = cantidad * precio * (1 - descuento)

if total < 50000:
    total += 5000

print("TOTAL: " , total)