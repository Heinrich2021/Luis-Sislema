import json

class AvesProduccion:
    def __init__(self, id_aves, tipo, cantidad, produccion_diaria):
        self.id_aves = id_aves
        self.tipo = tipo
        self.cantidad = cantidad
        self.produccion_diaria = produccion_diaria

    def __str__(self):
        return (f"ID: {self.id_aves}, Tipo: {self.tipo}, "
                f"Cantidad: {self.cantidad}, Producción diaria: {self.produccion_diaria}")

class InventarioAves:
    def __init__(self, archivo='inventario_aves.json'):
        self.lotes = {}
        self.archivo = archivo
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        try:
            with open(self.archivo, 'r') as f:
                self.lotes = json.load(f)
        except FileNotFoundError:
            print("Archivo de inventario no encontrado. Se creará uno nuevo al guardar.")
            self.lotes = {}
        except json.JSONDecodeError:
            print("Error al leer el archivo de inventario. Asegúrese de que el formato sea correcto.")
            self.lotes = {}

    def guardar_en_archivo(self):
        try:
            with open(self.archivo, 'w') as f:
                json.dump(self.lotes, f, indent=4)
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def añadir_lote(self, lote):
        if lote.id_aves in self.lotes:
            print("Lote ya existe.")
        else:
            self.lotes[lote.id_aves] = lote.__dict__
            self.guardar_en_archivo()
            print(f"Lote de {lote.tipo} añadido con éxito.")

    def eliminar_lote(self, id_aves):
        if id_aves in self.lotes:
            del self.lotes[id_aves]
            self.guardar_en_archivo()
            print(f"Lote {id_aves} eliminado.")
        else:
            print("Lote no encontrado.")

    def actualizar_lote(self, id_aves, cantidad=None, produccion_diaria=None):
        if id_aves in self.lotes:
            if cantidad is not None:
                self.lotes[id_aves]['cantidad'] = cantidad
            if produccion_diaria is not None:
                self.lotes[id_aves]['produccion_diaria'] = produccion_diaria
            self.guardar_en_archivo()
            print(f"Lote {id_aves} actualizado.")
        else:
            print("Lote no encontrado.")

    def buscar_lote_por_tipo(self, tipo):
        encontrados = [AvesProduccion(id_aves, info['tipo'], info['cantidad'], info['produccion_diaria'])
                       for id_aves, info in self.lotes.items() if tipo.lower() in info['tipo'].lower()]
        if encontrados:
            for lote in encontrados:
                print(lote)
        else:
            print(f"No se encontraron lotes con el tipo {tipo}.")

    def mostrar_lotes(self):
        if not self.lotes:
            print("El inventario de aves está vacío.")
        else:
            for id_aves, info in self.lotes.items():
                try:
                    lote = AvesProduccion(id_aves, info['tipo'], info['cantidad'], info['produccion_diaria'])
                    print(lote)
                except KeyError as e:
                    print(f"Error al mostrar el lote {id_aves}: falta el campo {e}.")

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
            id_aves = input("Ingrese ID del lote: ")
            tipo = input("Ingrese tipo de ave: ")
            cantidad = int(input("Ingrese cantidad de aves en el lote: "))
            produccion_diaria = float(input("Ingrese producción diaria (en unidades): "))
            lote = AvesProduccion(id_aves, tipo, cantidad, produccion_diaria)
            inventario.añadir_lote(lote)

        elif opción == "2":
            id_aves = input("Ingrese ID del lote a eliminar: ")
            inventario.eliminar_lote(id_aves)

        elif opción == "3":
            id_aves = input("Ingrese ID del lote a actualizar: ")
            cantidad = input("Ingrese nueva cantidad de aves (deje en blanco para no cambiar): ")
            produccion_diaria = input("Ingrese nueva producción diaria (deje en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            produccion_diaria = float(produccion_diaria) if produccion_diaria else None
            inventario.actualizar_lote(id_aves, cantidad, produccion_diaria)

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

if __name__ == "__main__":
    interfaz_usuario()

