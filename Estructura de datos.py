# Clase Aves_Produccion
# Se define un lote de aves con atributos id, tipo, cantidad, y produccion_diaria.

class AvesProduccion:
    def __init__(self, id, tipo, cantidad, produccion_diaria):
        """
        Constructor para la clase AvesProduccion.

        :para id: ID único del lote de aves
        :para tipo: Tipo de ave (e.g., gallina, pavo)
        :para cantidad: Cantidad de aves en el lote
        :para produccion_diaria: Producción diaria (e.g., huevos, carne) en unidades
        """
        self.id = id
        self.tipo = tipo
        self.cantidad = cantidad
        self.produccion_diaria = produccion_diaria

    # Métodos getter y setter para el ID
    # Métodos getter y setter permiten acceder y modificar estos atributos.

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    # Métodos getter y setter para el tipo
    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo

    # Métodos getter y setter para la cantidad
    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    # Métodos getter y setter para la producción diaria
    def get_produccion_diaria(self):
        return self.produccion_diaria

    def set_produccion_diaria(self, produccion_diaria):
        self.produccion_diaria = produccion_diaria

    # El método __str__ proporciona una representación legible del objeto.

    def __str__(self):
        """
        Representación en cadena del objeto AvesProduccion.
        """
        return (f"ID: {self.id}, Tipo: {self.tipo}, Cantidad: {self.cantidad}, "
                f"Producción Diaria: {self.produccion_diaria} unidades")


# Clase_InventarioAves
# Se gestiona una lista de lotes de aves, permitiendo añadir, eliminar, actualizar, buscar y mostrar los lotes.
# Se asegura de que cada ID sea único antes de añadir un nuevo lote al inventario.
class InventarioAves:
    def __init__(self):
        """
        Constructor para la clase InventarioAves.
        Inicializa una lista vacía para almacenar los lotes de aves.
        """
        self.lotes = []

    def añadir_lote(self, lote):
        """
        Añade un nuevo lote al inventario si el ID es único.

        :param lote: Instancia de la clase AvesProduccion a añadir
        """
        if any(l.get_id() == lote.get_id() for l in self.lotes):
            print(f"Error: El lote con ID {lote.get_id()} ya existe.")
        else:
            self.lotes.append(lote)
            print(f"Lote de {lote.get_tipo()} añadido con éxito.")

    def eliminar_lote(self, id):
        """
        Elimina un lote del inventario por su ID.

        :param id: ID del lote a eliminar
        """
        for lote in self.lotes:
            if lote.get_id() == id:
                self.lotes.remove(lote)
                print(f"Lote con ID {id} eliminado.")
                return
        print(f"Error: No se encontró lote con ID {id}.")

    def actualizar_lote(self, id, cantidad=None, produccion_diaria=None):
        """
        Actualiza la cantidad o la producción diaria de un lote por su ID.

        :param id: ID del lote a actualizar
        :param cantidad: Nueva cantidad de aves en el lote (opcional)
        :param produccion_diaria: Nueva producción diaria en unidades (opcional)
        """
        for lote in self.lotes:
            if lote.get_id() == id:
                if cantidad is not None:
                    lote.set_cantidad(cantidad)
                if produccion_diaria is not None:
                    lote.set_produccion_diaria(produccion_diaria)
                print(f"Lote con ID {id} actualizado.")
                return
        print(f"Error: No se encontró lote con ID {id}.")

    def buscar_lote_por_tipo(self, tipo):
        """
        Busca lotes por tipo de ave y muestra los encontrados.

        :param tipo: Tipo de ave a buscar (e.g., gallina, pavo)
        """
        encontrados = [l for l in self.lotes if tipo.lower() in l.get_tipo().lower()]
        if encontrados:
            for lote in encontrados:
                print(lote)
        else:
            print(f"No se encontraron lotes con el tipo {tipo}.")

    def mostrar_lotes(self):
        """
        Muestra todos los lotes en el inventario.
        """
        if self.lotes:
            for lote in self.lotes:
                print(lote)
        else:
            print("El inventario de aves está vacío.")

# Interfaz de Usuario
# Proporciona una interfaz de usuario en la consola para realizar operaciones sobre el inventario de aves.
# Permite al usuario gestionar lotes de aves mediante un menú interactivo.

def interfaz_usuario():
    """
    Función principal que proporciona un menú interactivo en la consola.
    """
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
