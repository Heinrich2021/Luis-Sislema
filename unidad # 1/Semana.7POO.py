# Esta clase tiene un constructor (__init__) que inicializa el nombre de la marca y el año de fundación.
# Cuando se crea una instancia de Marca, se imprime un mensaje indicando la creación de la marca.
class Marca:
    def __init__(self, nombre, fundacion):
        self.nombre = nombre
        self.fundacion = fundacion
        print(f"Marca '{self.nombre}' fundada en {self.fundacion}.")

    # El destructor (__del__) de Marca está configurado para imprimir un mensaje cuando se elimina la instancia de la marca.
    def __del__(self):
        print(f"Marca '{self.nombre}' eliminada.")


# Esta clase tiene un constructor (__init__) que inicializa el modelo de la motocicleta, el año y la instancia
# de Marca a la que pertenece.
# Cuando se crea una instancia de Motocicleta, se imprime un mensaje indicando la creación de la motocicleta y
# la marca a la que pertenece.

class Motocicleta:
    def __init__(self, modelo, anio, marca):
        self.modelo = modelo
        self.anio = anio
        self.marca = marca
        print(f"Motocicleta {self.modelo} del año {self.anio} creada, de la marca '{self.marca.nombre}'.")

    # El destructor (__del__) de Motocicleta está configurado para imprimir un mensaje cuando
    # se elimina la instancia de la motocicleta.
    def __del__(self):
        print(f"Motocicleta {self.modelo} del año {self.anio} eliminada.")


# Creación de instancias de Marca y Motocicleta

mi_marca = Marca("Honda", 1948)
mi_motocicleta = Motocicleta("CBR1000RR", 2023, mi_marca)

# Eliminando instancias

del mi_motocicleta
del mi_marca
