import re

class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}, Categoría: {self.categoria}, ISBN: {self.isbn}"

class Usuario:
    def __init__(self, nombre, id_usuario, cedula):
        self.nombre = nombre
        if self.validar_id(id_usuario):
            self.id_usuario = id_usuario
        else:
            raise ValueError("El ID del usuario debe contener letras y números.")
        self.cedula = cedula
        self.libros_prestados = []

    def __str__(self):
        return f"Nombre: {self.nombre}, ID: {self.id_usuario}, Cédula: {self.cedula}, Libros Prestados: {self.libros_prestados}"

    @staticmethod
    def validar_id(id_usuario):
        # Verificar que el ID contenga al menos una letra y un número
        return bool(re.match(r'^(?=.*[a-zA-Z])(?=.*\d)', id_usuario))

class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}
        self.max_usuarios = 12

    def añadir_libro(self, libro):
        self.libros[libro.isbn] = libro

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
        else:
            print(f"El libro con ISBN {isbn} no se encuentra en la biblioteca.")

    def registrar_usuario(self, usuario):
        if len(self.usuarios) < self.max_usuarios:
            if usuario.cedula not in self.usuarios:
                self.usuarios[usuario.cedula] = usuario
            else:
                print(f"El usuario con cédula {usuario.cedula} ya está registrado.")
        else:
            print("No se pueden registrar más usuarios. Límite alcanzado.")

    def dar_baja_usuario(self, cedula):
        if cedula in self.usuarios:
            del self.usuarios[cedula]
        else:
            print(f"Usuario con cédula {cedula} no encontrado.")

    def prestar_libro(self, cedula, isbn):
        if cedula in self.usuarios:
            usuario = self.usuarios[cedula]
            if isbn in self.libros and self.libros[isbn].categoria == "Veterinaria":
                usuario.libros_prestados.append(isbn)
                print(f"Libro {isbn} prestado a {usuario.nombre}.")
            else:
                print(f"El libro no está disponible o no es de la categoría 'Veterinaria'.")
        else:
            print("Usuario no registrado o no autorizado.")

    def devolver_libro(self, cedula, isbn):
        if cedula in self.usuarios:
            usuario = self.usuarios[cedula]
            if isbn in usuario.libros_prestados:
                usuario.libros_prestados.remove(isbn)
                print(f"Libro {isbn} devuelto por {usuario.nombre}.")
            else:
                print(f"El usuario {usuario.nombre} no tiene prestado el libro con ISBN {isbn}.")
        else:
            print("Usuario no registrado.")

    def buscar_libros(self, titulo=None, autor=None, categoria=None):
        resultados = []
        for libro in self.libros.values():
            if (titulo and titulo.lower() in libro.titulo.lower()) or \
               (autor and autor.lower() in libro.autor.lower()) or \
               (categoria and categoria.lower() in libro.categoria.lower()):
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, cedula):
        if cedula in self.usuarios:
            usuario = self.usuarios[cedula]
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for isbn in usuario.libros_prestados:
                    print(self.libros[isbn])
            else:
                print(f"{usuario.nombre} no tiene libros prestados.")
        else:
            print("Usuario no registrado.")

# Ejemplo de uso
if __name__ == "__main__":
    biblioteca = Biblioteca()

    # Agregar libros
    libro1 = Libro("Manual de Veterinaria", "Autor A", "Veterinaria", "ISBN001")
    libro2 = Libro("Historia de la Medicina", "Autor B", "Medicina", "ISBN002")
    biblioteca.añadir_libro(libro1)
    biblioteca.añadir_libro(libro2)

    # Registrar usuarios
    usuario1 = Usuario("Enrique Guaman", "Enrique123", "0012345678")
    usuario2 = Usuario("Mario Lopez", "mario456", "0023456789")
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Prestar libros
    biblioteca.prestar_libro("0012345678", "ISBN001")  # Libro de Veterinaria
    biblioteca.prestar_libro("0012345678", "ISBN002")  # Libro de Medicina (no permitido)
