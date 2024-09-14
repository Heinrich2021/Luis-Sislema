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

        self.lista_registros = tk.Listbox(root)
        self.lista_registros.pack(fill=tk.BOTH, expand=True)

        self.registros = {}
     # Al hacer clic en "Registrar Entrada", se guarda la hora actual para el empleado.
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
    # Al hacer clic en "Registrar Salida", se guarda la hora de salida, siempre y cuando haya una entrada registrada previamente.
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
     # Menú Limpiar Registros: Permite borrar todos los registros.
    def limpiar(self):
        self.registros.clear()
        self.lista_registros.delete(0, tk.END)
     # Se muestra en una Listbox el nombre del empleado junto con sus horarios de entrada y salida.
    def actualizar_lista(self):
        self.lista_registros.delete(0, tk.END)
        for nombre, tiempos in self.registros.items():
            self.lista_registros.insert(tk.END, f"Nombre: {nombre} | Entrada: {tiempos['entrada']} | Salida: {tiempos['salida']}")


if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionAsistencia(root)
    root.mainloop()
