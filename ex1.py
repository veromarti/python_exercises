# 1. Panadería de Don Pancho — Descuentos por cantidades
# La panadería de Don Pancho vende pan a $300 cada uno.

# Reglas:

# Si compra más de 20 panes → 10% descuento
# Si compra más de 50 panes → 20% descuento
# Si ingresa una cantidad negativa, mostrar "Cantidad inválida"
# Calcular y mostrar el total.

valor_pan = 300
cantidad = int(input("Ingrese la cantidad de panes que desea comprar: "))
total = 0

if cantidad > 20:
    
    if cantidad > 50:
        descuento = 0.2
    else:
        descuento = 0.1
    total = cantidad * valor_pan * (1 - descuento)
    
elif cantidad < 0:
    print("Cantidad inválida")
    
else:
    total = cantidad * valor_pan
    
print("El total a pagar es: $", total, " por la compra de ", cantidad, " panes.")

