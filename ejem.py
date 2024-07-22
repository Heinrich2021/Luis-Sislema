# Definición de Clases

# Clase Base: Marca
class Marca:
    def __init__(self, nombre, pais_origen):
        self.nombre = nombre
        self.pais_origen = pais_origen

    def mostrar_informacion(self):
        return f"Marca: {self.nombre}, País de Origen: {self.pais_origen}"

# Clase Derivada: Motociclista
class Motociclista(Marca):
    def __init__(self, nombre, pais_origen, nombre_motociclista, edad, licencia):
        super().__init__(nombre, pais_origen)
        self.nombre_motociclista = nombre_motociclista
        self.edad = edad
        self.licencia = licencia

    def mostrar_informacion(self):
        informacion_base = super().mostrar_informacion()
        return f"{informacion_base}, Nombre del Motociclista: {self.nombre_motociclista}, Edad: {self.edad}, Licencia: {self.licencia}"

# Clase con Encapsulación: marca
class marca:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__motociclistas = []

    def agregar_motociclista(self, motociclista):
        if isinstance(motociclista, Motociclista):
            self.__motociclistas.append(motociclista)
            print(f"Motociclista {motociclista.nombre_motociclista} agregado a la marca {self.__nombre}.")
        else:
            print("Solo se pueden agregar instancias de la clase Motociclista.")

    def mostrar_motociclistas(self):
        for motociclista in self.__motociclistas:
            print(motociclista.mostrar_informacion())

    def obtener_nombre(self):
        return self.__nombre

    def cambiar_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

# Polimorfismo
def mostrar_identidad(marca):
    print(marca.mostrar_informacion())

# Creación de Objetos y Ejecución

# Creando objetos de las clases
marca1 = Marca("Yamaha", "Japón")
motociclista1 = Motociclista("Honda", "Japón", "Luis", 30, "A12345")
motociclista2 = Motociclista("BMW", "Alemania", "Ana", 28, "B67890")

# Usando polimorfismo
mostrar_identidad(marca1)
# Output: Marca: Yamaha, País de Origen: Japón
mostrar_identidad(motociclista1)
# Output: Marca: Honda, País de Origen: Japón, Nombre del Motociclista: Luis, Edad: 30, Licencia: A12345

# Creando una instancia de marca y agregando motociclistas
marca1 = marca(" 1")
marca1.agregar_motociclista(motociclista1)
marca1.agregar_motociclista(motociclista2)

# Mostrando motociclistas de la marca
marca1.mostrar_motociclistas()

# Cambiando el nombre de la marca
marca1.cambiar_nombre("Platina")
print(f"Nuevo nombre de la marca: {marca1.obtener_nombre()}")
