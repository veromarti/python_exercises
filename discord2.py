# 2. Cine “La Estrella” — Tarifas por edad
# Pedir la edad del cliente:

# Edad	    Precio
# < 5 años:	Entrada gratis
# 5 a 11:	$5.000
# 12 a 59:	$8.000
# ≥ 60: 	$4.000 (descuento adulto mayor)
# Mostrar el precio.
# Si la edad es negativa, mostrar error.

edad = int(input("Ingrese la edad del cliente: "))
#valor_entrada = 0
total = 0

if 0 <= edad < 100:
    
    if edad < 5:
        print("El valor de la entrada es: $0 (Entrada gratis)")
    elif 5 <= edad <= 11:
        print("El valor de la entrada es: $5.000")
    elif 12 <= edad <= 59:
        print("El valor de la entrada es: $8.000")
    elif  edad >= 60:
        print("El valor de la entrada es: $4.000 (descuento de adulto mayor)")
    
elif edad < 0:
    print("Error: La edad no puede ser menor que cero")
    
else:
    pass
