# 7. Restaurante “El Sabor Colombiano” — Menú + bebida opcional + IVA
# Menú: $12.000

# Opciones bebida:

# sí → $3.000
# no → $0
# Luego aplicar IVA del 8% al total final.
# Mostrar valor con IVA incluido.

menu = 12000
bebida = 3000
iva = 0.08
opcion = input("¿Desea agregar bebida a su pedido? (s/n): ").lower()

total = 0

if opcion == "s":
    total = menu + bebida
elif opcion == "n":
    total = menu
else:
    pass    

print("Subtotal sin IVA: $", total)
print("Total con IVA incluido: $", int(total * (1 + iva)))
