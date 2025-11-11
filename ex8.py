# 8. Empresa “TecnoPlus” — Evaluación compuesta
# El usuario ingresa dos notas (0.0 - 5.0):

# Prueba técnica (70%)
# Prueba lógica (30%)
# Cálculo: nota_final = (tecnica * 0.7) + (logica * 0.3)

# Condiciones:

# nota_final ≥ 3 → “Aprobado”
# 2 ≤ nota_final < 3 → “Revisión”
# < 2 → “Reprobado”
# Validar que las notas estén en rango.

nota_final = 0.0
tecnica = float(input("Ingrese la nota de la prueba técnica (0.0 - 5.0): "))
logica = float(input("Ingrese la nota de la prueba lógica (0.0 - 5.0): "))

if 0.0 <= tecnica <= 5.0 and 0.0 <= logica <= 5.0:
    nota_final = (tecnica * 0.7) + (logica * 0.3)
    
    if nota_final >= 3.0:
        print("Estado: Aprobado")
    elif 2.0 <= nota_final < 3.0:
        print("Estado: Revisión")
    else:
        print("Estado: Reprobado")
else:
    print("Error: Las notas deben estar en el rango de 0.0 a 5.0")
