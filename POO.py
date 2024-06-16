# Implementación en Programación Orientada a Objetos (POO)

class ClimaDiario:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperatura_diaria(self, temperatura):
        self.temperaturas.append(temperatura)

    def calcular_promedio_semanal(self):
        promedios_semana = []
        semana_actual = []
        for i, temperatura in enumerate(self.temperaturas):
            semana_actual.append(temperatura)
            if (i + 1) % 7 == 0:  # Cada 7 días (semana completa)
                promedio_semana = sum(semana_actual) / len(semana_actual)
                promedios_semana.append(promedio_semana)
                semana_actual = []
        return promedios_semana

# Ejemplo de uso:
clima_mayo = ClimaDiario()

# Suponemos ingreso manual de temperaturas para simplificar el ejemplo
temperaturas = [22.5, 24.3, 23.8, 25.1, 26.7, 27.2, 28.4, 29.0, 28.3, 27.6,
                26.9, 25.5, 24.8, 23.7, 22.9, 22.3, 21.8, 21.4, 20.9, 20.5,
                19.9, 19.6, 19.3, 18.8, 18.5, 18.2, 17.9, 17.6, 17.4, 17.2, 17.0]

for dia, temperatura in enumerate(temperaturas, start=1):
    clima_mayo.ingresar_temperatura_diaria(temperatura)

promedios_semana = clima_mayo.calcular_promedio_semanal()

print("\nPromedios semanales del mes de mayo:")
for i, promedio in enumerate(promedios_semana):
    print(f"Semana {i + 1}: {promedio:.2f}")
