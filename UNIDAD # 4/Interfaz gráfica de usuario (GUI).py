import tkinter as tk
from tkinter import messagebox
from datetime import datetime


class AplicacionAsistencia:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Asistencia")
        # Ajusta el tamaño de la ventana
        self.root.geometry("400x400")
        # Crear menú
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        # Menú de archivo
        self.archivo_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Archivo", menu=self.archivo_menu)
        self.archivo_menu.add_command(label="Limpiar Registros", command=self.limpiar)
        self.archivo_menu.add_separator()
        self.archivo_menu.add_command(label="Salir", command=self.root.quit)

        # Componentes GUI
        self.etiqueta_nombre = tk.Label(root, text="Nombre del Empleado:")
        self.etiqueta_nombre.pack()

        self.entrada_nombre = tk.Entry(root)
        self.entrada_nombre.pack()

        self.boton_entrada = tk.Button(root, text="Registrar Entrada", command=self.registrar_entrada)
        self.boton_entrada.pack()

        self.boton_salida = tk.Button(root, text="Registrar Salida", command=self.registrar_salida)
        self.boton_salida.pack()

        self.lista_registros = tk.Listbox(root, selectmode=tk.SINGLE)
        self.lista_registros.pack(fill=tk.BOTH, expand=True)

        self.registros = {}

        # Nuevos elementos para agregar información
        self.etiqueta_info = tk.Label(root, text="Información adicional:")
        self.etiqueta_info.pack()

        self.entrada_info = tk.Entry(root)
        self.entrada_info.pack()

        self.boton_agregar = tk.Button(root, text="Agregar Información", command=self.agregar_informacion)
        self.boton_agregar.pack()

        self.boton_limpiar = tk.Button(root, text="Limpiar Selección", command=self.limpiar_seleccion)
        self.boton_limpiar.pack()

    # Registrar la entrada del empleado
    def registrar_entrada(self):
        nombre = self.entrada_nombre.get()
        if nombre != "":
            hora_entrada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if nombre not in self.registros:
                self.registros[nombre] = {'entrada': hora_entrada, 'salida': 'No registrada'}
                self.actualizar_lista()
            else:
                messagebox.showwarning("Advertencia", "Ya has registrado la entrada para este empleado.")
        else:
            messagebox.showwarning("Advertencia", "El campo de nombre está vacío.")

    # Registrar la salida del empleado
    def registrar_salida(self):
        nombre = self.entrada_nombre.get()
        if nombre != "":
            if nombre in self.registros and self.registros[nombre]['salida'] == 'No registrada':
                hora_salida = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.registros[nombre]['salida'] = hora_salida
                self.actualizar_lista()
            else:
                messagebox.showwarning("Advertencia", "No se puede registrar la salida sin una entrada previa.")
        else:
            messagebox.showwarning("Advertencia", "El campo de nombre está vacío.")

    # Limpiar los registros
    def limpiar(self):
        self.registros.clear()
        self.lista_registros.delete(0, tk.END)

    # Actualizar la lista con la información de entrada y salida
    def actualizar_lista(self):
        self.lista_registros.delete(0, tk.END)
        for nombre, tiempos in self.registros.items():
            self.lista_registros.insert(tk.END, f"Nombre: {nombre} | Entrada: {tiempos['entrada']} | Salida: {tiempos['salida']}")

    # Agregar información adicional
    def agregar_informacion(self):
        info = self.entrada_info.get()
        if info:
            self.lista_registros.insert(tk.END, f"Información adicional: {info}")
            self.entrada_info.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "El campo de información está vacío.")

    # Limpiar la selección en la lista
    def limpiar_seleccion(self):
        seleccion = self.lista_registros.curselection()
        if seleccion:
            self.lista_registros.delete(seleccion)
        else:
            messagebox.showwarning("Advertencia", "No hay ningún elemento seleccionado para borrar.")


if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionAsistencia(root)
    root.mainloop()
