# Implementación en Programación Tradicional

def ingresar_temperaturas_diarias():
    temperaturas = []
    for dia in range(1, 31):  # Suponemos un mes completo (del 1 al 30)
        temperatura = float(input(f"Ingrese la temperatura del día {dia} de junio: "))
        temperaturas.append(temperatura)
    return temperaturas

def calcular_promedio_semanal(temperaturas):
    promedios_semana = []
    semana_actual = []
    for i, temperatura in enumerate(temperaturas):
        semana_actual.append(temperatura)
        if (i + 1) % 7 == 0 or (i + 1) == len(temperaturas):  # Cada 7 días o al final del mes
            promedio_semana = sum(semana_actual) / len(semana_actual)
            promedios_semana.append(promedio_semana)
            semana_actual = []
    return promedios_semana

# Ejemplo de uso:
temperaturas_junio = ingresar_temperaturas_diarias()
promedios_semana = calcular_promedio_semanal(temperaturas_junio)

print("\nPromedios semanales del mes de junio:")
for i, promedio in enumerate(promedios_semana):
    print(f"Semana {i + 1}: {promedio:.2f}")