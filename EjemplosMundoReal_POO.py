class Avion:
    def __init__(self, modelo, numero_serie):
        self.modelo = modelo
        self.numero_serie = numero_serie
        self.piloto = None
        self.armas = []
        self.sistemas_defensa = []

    def asignar_piloto(self, piloto):
        self.piloto = piloto

    def agregar_arma(self, arma):
        self.armas.append(arma)

    def agregar_sistema_defensa(self, sistema):
        self.sistemas_defensa.append(sistema)

    def mostrar_estado(self):
        print(f"Modelo: {self.modelo}, Número de serie: {self.numero_serie}")
        if self.piloto:
            print(f"Piloto asignado: {self.piloto.nombre}")
        else:
            print("No hay piloto asignado.")
        print(f"Armas: {[arma.nombre for arma in self.armas]}")
        print(f"Sistemas de Defensa: {[sistema.nombre for sistema in self.sistemas_defensa]}")


class Piloto:
    def __init__(self, nombre, rango, horas_vuelo):
        self.nombre = nombre
        self.rango = rango
        self.horas_vuelo = horas_vuelo

    def incrementar_horas_vuelo(self, horas):
        self.horas_vuelo += horas
class SistemaDefensa:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
class Arma:
    def __init__(self, nombre, calibre, tipo):
        self.nombre = nombre
        self.calibre = calibre
        self.tipo = tipo


class Pista:
    def __init__(self, numero, longitud):
        self.numero = numero
        self.longitud = longitud
        self.ocupada = False

    def ocupar(self):
        self.ocupada = True

    def liberar(self):
        self.ocupada = False


class Angar:
    def __init__(self, numero):
        self.numero = numero
        self.avion = None

    def almacenar_avion(self, avion):
        self.avion = avion

    def liberar_avion(self):
        self.avion = None


class SimuladorVuelo:
    def __init__(self, piloto):
        self.piloto = piloto

    def simular_vuelo(self, horas):
        print(f"Simulando vuelo para {self.piloto.nombre} durante {horas} horas.")
        self.piloto.incrementar_horas_vuelo(horas)
        print(f"Horas de vuelo totales: {self.piloto.horas_vuelo}")


# Crear instancias de cada clase
piloto1 = Piloto("Luis Sislema", "Teniente", 120)
avion1 = Avion("F-16", "12345A")
sistema_defensa1 = SistemaDefensa("Chaff", "Contramedida")
arma1 = Arma("Misil AIM-120", "120mm", "Misil Aire-Aire")
pista1 = Pista(1, 3000)
angar1 = Angar(1)

# Asignar piloto al avión
avion1.asignar_piloto(piloto1)

# Agregar armas y sistemas de defensa al avión
avion1.agregar_arma(arma1)
avion1.agregar_sistema_defensa(sistema_defensa1)

# Mostrar estado del avión
avion1.mostrar_estado()

# Almacenar el avión en el angar
angar1.almacenar_avion(avion1)

# Simular un vuelo
simulador = SimuladorVuelo(piloto1)
simulador.simular_vuelo(5)
