# 6. Parqueadero “RapidCar” — Tarifa escalonada
# Tarifa:

# 0 a 5 horas: $2.000 x hora
# > 5 horas: $2.000 x hora + multa fija de $5.000

# Validar horas:

# No permitir números negativos.
# Mostrar valor total.

tarifa = 2000
multa = 5000

horas = int(input("Ingrese la cantidad de horas que el vehículo estuvo estacionado: "))

if (0 < horas <= 5):
    total = horas * tarifa
    print("El valor total a pagar es: $", total)

elif horas > 5:
    total = (horas * tarifa) + multa
    print("El valor total a pagar es: $", total)

else:
    print("Error: La cantidad de horas no puede ser negativa o cero")
