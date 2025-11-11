# 3. Gimnasio “Solo Leveling Fit” — Motivación + Bono
# Pedir cuántos días entrenó esta semana.

# ≥ 4 días → "¡Excelente disciplina!" + gana 1 punto de energía
# 2 o 3 → "Bien, pero puedes dar más"
# 0 o 1 → "No aflojes, tú puedes mejorar"
# Mostrar mensaje y si aplica, los puntos ganados.

puntos_energia = 0

dias_entrenados = int(input("Ingrese la cantidad de días que entrenó esta semana: "))

if dias_entrenados >= 4:
    print("¡Excelente disciplina!")
    puntos_energia += 1
    print("Has ganado 1 punto de energía. Total de puntos de energía:", puntos_energia)
    
elif 2 <= dias_entrenados <= 3:
    print("Bien, pero puedes dar más")
    
elif 0 <= dias_entrenados <= 1:
    print("No aflojes, tú puedes mejorar")
