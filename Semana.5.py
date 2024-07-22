# Este programa simula una carrera de motocicletas en la ruta Puyo-Tena

class Motocicleta:
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima  # en km/h

    def mostrar_informacion(self):
        return f"Motocicleta: {self.marca} {self.modelo}, Velocidad Máxima: {self.velocidad_maxima} km/h"

class Piloto:
    def __init__(self, nombre, edad, experiencia):
        self.nombre = nombre
        self.edad = edad
        self.experiencia = experiencia  # en años

    def mostrar_informacion(self):
        return f"Piloto: {self.nombre}, Edad: {self.edad}, Experiencia: {self.experiencia} años"

class Pista:
    def __init__(self, nombre, distancia):
        self.nombre = nombre
        self.distancia = distancia  # en km

    def mostrar_informacion(self):
        return f"Pista: {self.nombre}, Distancia: {self.distancia} km"

def iniciar_ruta(pilotos, motocicletas, pista):
    print("Iniciando la ruta Puyo-Tena...\n")
    tiempos_de_llegada = []

    for i in range(len(pilotos)):
        piloto = pilotos[i]
        motocicleta = motocicletas[i]
        tiempo_llegada = pista.distancia / motocicleta.velocidad_maxima
        tiempos_de_llegada.append((piloto.nombre, tiempo_llegada))

        print(piloto.mostrar_informacion())
        print(motocicleta.mostrar_informacion())
        print(f"Tiempo estimado de llegada: {tiempo_llegada:.2f} horas\n")

    ganador = min(tiempos_de_llegada, key=lambda x: x[1])
    print(f"El ganador es {ganador[0]} con un tiempo de llegada de {ganador[1]:.2f} horas.")

# Constantes
DISTANCIA_PISTA = 100  # en km

# Crear instancias de motocicletas
motocicletas = [
    Motocicleta("Yamaha", "YZF-R1", 299),
    Motocicleta("Honda", "CBR600RR", 250),
    Motocicleta("Kawasaki", "Ninja ZX-6R", 260),
    Motocicleta("Ducati", "Panigale V4", 300),
    Motocicleta("BMW", "S1000RR", 305),
    Motocicleta("Suzuki", "GSX-R1000", 290)
]

# Crear instancias de pilotos
pilotos = [
    Piloto("Carlos", 30, 10),
    Piloto("Luis", 25, 5),
    Piloto("Juan", 28, 7),
    Piloto("Miguel", 35, 12),
    Piloto("Andrés", 27, 6),
    Piloto("Jorge", 32, 11)
]

# Crear instancia de la pista
pista_puyo_tena = Pista("Ruta Puyo-Tena", DISTANCIA_PISTA)

# Iniciar la ruta
iniciar_ruta(pilotos, motocicletas, pista_puyo_tena)
