# Clase Aves-Produccion
class AvesProduccion:
    def __init__(self, id, tipo, cantidad, produccion_diaria):
        self.id = id
        self.tipo = tipo
        self.cantidad = cantidad
        self.produccion_diaria = produccion_diaria

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_produccion_diaria(self):
        return self.produccion_diaria

    def set_produccion_diaria(self, produccion_diaria):
        self.produccion_diaria = produccion_diaria

    def __str__(self):
        return (f"ID: {self.id}, Tipo: {self.tipo}, Cantidad: {self.cantidad}, "
                f"Producción Diaria: {self.produccion_diaria} unidades")

# Clase InventarioAves
# El inventario se carga desde inventario.txt al iniciar el programa.
# Si el archivo no existe, se crea cuando se guarda un lote por primera vez.

class InventarioAves:
    def __init__(self, archivo='inventario.txt'):
        self.lotes = []
        self.archivo = archivo
        self.cargar_desde_archivo()
#Se manejan excepciones como ´FileNotFoundError´, ´PermissionError´, y otras posibles excepciones durante la lectura y escritura de archivos.
    def cargar_desde_archivo(self):
        try:
            with open(self.archivo, 'r') as archivo:
                for linea in archivo:
                    id, tipo, cantidad, produccion_diaria = linea.strip().split(',')
                    self.lotes.append(AvesProduccion(id, tipo, int(cantidad), float(produccion_diaria)))
        except FileNotFoundError:
            print(f"El archivo {self.archivo} no existe. Se creará uno nuevo al guardar cambios.")
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")

    def guardar_en_archivo(self):
        try:
            with open(self.archivo, 'w') as archivo:
                for lote in self.lotes:
                    archivo.write(f"{lote.get_id()},{lote.get_tipo()},{lote.get_cantidad()},{lote.get_produccion_diaria()}\n")
        except PermissionError:
            print(f"Error: No se tiene permiso para escribir en el archivo {self.archivo}.")
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")

    def añadir_lote(self, lote):
        if any(l.get_id() == lote.get_id() for l in self.lotes):
            print(f"Error: El lote con ID {lote.get_id()} ya existe.")
        else:
            self.lotes.append(lote)
            self.guardar_en_archivo()
            print(f"Lote de {lote.get_tipo()} añadido con éxito.")

    def eliminar_lote(self, id):
        for lote in self.lotes:
            if lote.get_id() == id:
                self.lotes.remove(lote)
                self.guardar_en_archivo()
                print(f"Lote con ID {id} eliminado.")
                return
        print(f"Error: No se encontró lote con ID {id}.")

    def actualizar_lote(self, id, cantidad=None, produccion_diaria=None):
        for lote in self.lotes:
            if lote.get_id() == id:
                if cantidad is not None:
                    lote.set_cantidad(cantidad)
                if produccion_diaria is not None:
                    lote.set_produccion_diaria(produccion_diaria)
                self.guardar_en_archivo()
                print(f"Lote con ID {id} actualizado.")
                return
        print(f"Error: No se encontró lote con ID {id}.")

    def buscar_lote_por_tipo(self, tipo):
        encontrados = [l for l in self.lotes if tipo.lower() in l.get_tipo().lower()]
        if encontrados:
            for lote in encontrados:
                print(lote)
        else:
            print(f"No se encontraron lotes con el tipo {tipo}.")

    def mostrar_lotes(self):
        if self.lotes:
            for lote in self.lotes:
                print(lote)
        else:
            print("El inventario de aves está vacío.")

# Interfaz de Usuario
# La interfaz permite al usuario gestionar los lotes y muestra mensajes de éxito o error según las operaciones realizadas.
def interfaz_usuario():
    inventario = InventarioAves()

    while True:
        print("\nSistema de Gestión de Aves de Producción")
        print("1. Añadir lote de aves")
        print("2. Eliminar lote de aves")
        print("3. Actualizar lote de aves")
        print("4. Buscar lote por tipo de ave")
        print("5. Mostrar todos los lotes")
        print("6. Salir")

        opción = input("Elija una opción: ")

        if opción == "1":
            id = input("Ingrese ID del lote: ")
            tipo = input("Ingrese tipo de ave: ")
            cantidad = int(input("Ingrese cantidad de aves en el lote: "))
            produccion_diaria = float(input("Ingrese producción diaria (en unidades): "))
            lote = AvesProduccion(id, tipo, cantidad, produccion_diaria)
            inventario.añadir_lote(lote)

        elif opción == "2":
            id = input("Ingrese ID del lote a eliminar: ")
            inventario.eliminar_lote(id)

        elif opción == "3":
            id = input("Ingrese ID del lote a actualizar: ")
            cantidad = input("Ingrese nueva cantidad de aves (deje en blanco para no cambiar): ")
            produccion_diaria = input("Ingrese nueva producción diaria (deje en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            produccion_diaria = float(produccion_diaria) if produccion_diaria else None
            inventario.actualizar_lote(id, cantidad, produccion_diaria)

        elif opción == "4":
            tipo = input("Ingrese tipo de ave a buscar: ")
            inventario.buscar_lote_por_tipo(tipo)

        elif opción == "5":
            inventario.mostrar_lotes()

        elif opción == "6":
            print("Saliendo del sistema.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar la interfaz de usuario cuando se ejecute el script
if __name__ == "__main__":
    interfaz_usuario()
