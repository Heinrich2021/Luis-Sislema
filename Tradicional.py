# Definición de funciones

def ingresar_temperaturas_diarias():
    """ Función para ingresar las temperaturas diarias de junio """
    temperaturas = []
    for dia in range(1, 31):  # Suponiendo junio tiene 30 días
        temp = float(input(f"Ingrese la temperatura del día {dia} de junio: "))
        temperaturas.append(temp)
    return temperaturas


def calcular_promedio_semanal(temperaturas):
    """ Función para calcular el promedio semanal de temperaturas """
    promedios_semanales = []
    semana_actual = []

    for i in range(len(temperaturas)):
        semana_actual.append(temperaturas[i])

        # Cada semana tiene 7 días
        if len(semana_actual) == 7 or i == len(temperaturas) - 1:
            promedio_semana = sum(semana_actual) / len(semana_actual)
            promedios_semanales.append(promedio_semana)
            semana_actual = []  # Reiniciar la lista para la siguiente semana

    return promedios_semanales


def imprimir_promedios(promedios_semanales):
    """ Función para imprimir los promedios semanales """
    print("\nPromedios semanales de temperaturas de junio:")
    for i, promedio in enumerate(promedios_semanales):
        print(f"Semana {i + 1}: {promedio:.2f} °C")


# Programa principal

def main():
    temperaturas_junio = ingresar_temperaturas_diarias()
    promedios_semanales = calcular_promedio_semanal(temperaturas_junio)
    imprimir_promedios(promedios_semanales)


if __name__ == "__main__":
    main()
