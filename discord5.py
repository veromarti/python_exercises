# 5. Librería “El Saber” — Descuento estudiante + cupón
# Libro cuesta $25.000.

# Si es estudiante → 15% descuento
# Si además tiene cupón "LIBRO10" → 10% adicional sobre el valor ya descontado
# Validar:

# Si no es estudiante, el cupón no aplica.
# Si ingresa cupón incorrecto, ignorarlo.
# Mostrar total.

precio_libro =25000
descuento = 0
estudiante = input("¿Es usted estudiante? (s/n): ").lower()
cupon = input("Tiene cupon de descuento? (s/n): ").lower()
codigo_cupon = ""

#cupon = input("Ingrese el cupón si tiene (o presione Enter para omitir): ").strip()

if estudiante == "s":
    descuento += 0.15  

elif estudiante == "n":
    descuento += 0
    
else:
    pass
    
if cupon == "s":
    codigo_cupon = input("Ingrese el código del cupón: ").strip()
    if codigo_cupon == "LIBRO10":
        descuento += 0.10 
    else:
        print("Cupón inválido, no se aplicará descuento adicional.")
else:
    pass

total = precio_libro * (1 - descuento)
print("El total a pagar es: $", total)