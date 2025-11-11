# 10. Club “Noche Estelar” — Acceso + validación documento
# Pedir edad y documento.

# Reglas:

# Edad ≥ 18 → puede entrar solo si tiene documento.
# Si la edad < 18 → "Entrada denegada"
# Si tiene 18 o más pero no tiene documento → "Debe presentar documento"

age = int(input("Ingrese su edad: "))

if (0 < age < 18):
    print("Entrada denegada")
elif (18 <= age < 100):
    documento = input("¿Tiene documento? (S/N): ").lower()
    
    if documento == "s":
        print("Puede entrar")
    elif documento == "n":
        print("Debe presentar documento")
        
else:
    pass