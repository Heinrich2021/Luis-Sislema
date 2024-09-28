import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime


class AplicacionAsistencia:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Asistencia y Tareas")
        self.root.geometry("700x700")

        # Crear menú
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        # Menú de archivo
        self.archivo_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Archivo", menu=self.archivo_menu)
        self.archivo_menu.add_command(label="Limpiar Registros", command=self.limpiar_registros)
        self.archivo_menu.add_separator()
        self.archivo_menu.add_command(label="Salir", command=self.root.quit)

        # SECCIÓN DE ASISTENCIA

        # Componentes GUI para asistencia
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

        # Nuevos elementos para agregar información adicional
        self.etiqueta_info = tk.Label(root, text="Información adicional:")
        self.etiqueta_info.pack()

        self.entrada_info = tk.Entry(root)
        self.entrada_info.pack()

        self.boton_agregar = tk.Button(root, text="Agregar Información", command=self.agregar_informacion)
        self.boton_agregar.pack()

        self.boton_limpiar = tk.Button(root, text="Limpiar Selección", command=self.limpiar_seleccion)
        self.boton_limpiar.pack()

        # SECCIÓN DE TAREAS

        # Campo de entrada para nuevas tareas
        self.etiqueta_tarea = tk.Label(root, text="Nombre de la Tarea:")
        self.etiqueta_tarea.pack()

        self.entrada_tarea = tk.Entry(root)
        self.entrada_tarea.pack()

        self.boton_añadir_tarea = tk.Button(root, text="Añadir Tarea", command=self.añadir_tarea)
        self.boton_añadir_tarea.pack()

        # Treeview para mostrar tareas ingresadas
        self.treeview = ttk.Treeview(root, columns=('Tarea', 'Estado'), show='headings')
        self.treeview.heading('Tarea', text='Tareas')
        self.treeview.heading('Estado', text='Estado')
        self.treeview.pack(pady=10, fill=tk.BOTH, expand=True)

        self.boton_marcar_completada = tk.Button(root, text="Marcar como Completada", command=self.marcar_completada)
        self.boton_marcar_completada.pack()

        # Vincular eventos de teclado
        self.entrada_tarea.bind("<Return>", lambda event: self.añadir_tarea())
        self.root.bind("<Escape>", self.on_escape_pressed)

    # FUNCIONES DE ASISTENCIA

    def registrar_entrada(self):
        nombre = self.entrada_nombre.get()
        if nombre != "":
            hora_entrada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if nombre not in self.registros:
                self.registros[nombre] = {'entrada': hora_entrada, 'salida': 'No registrada'}
                self.actualizar_lista_asistencia()
            else:
                messagebox.showwarning("Advertencia", "Ya has registrado la entrada para este empleado.")
        else:
            messagebox.showwarning("Advertencia", "El campo de nombre está vacío.")

    def registrar_salida(self):
        nombre = self.entrada_nombre.get()
        if nombre != "":
            if nombre in self.registros and self.registros[nombre]['salida'] == 'No registrada':
                hora_salida = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.registros[nombre]['salida'] = hora_salida
                self.actualizar_lista_asistencia()
            else:
                messagebox.showwarning("Advertencia", "No se puede registrar la salida sin una entrada previa.")
        else:
            messagebox.showwarning("Advertencia", "El campo de nombre está vacío.")

    def actualizar_lista_asistencia(self):
        self.lista_registros.delete(0, tk.END)
        for nombre, tiempos in self.registros.items():
            self.lista_registros.insert(tk.END, f"Nombre: {nombre} | Entrada: {tiempos['entrada']} | Salida: {tiempos['salida']}")

    def agregar_informacion(self):
        info = self.entrada_info.get()
        if info:
            self.lista_registros.insert(tk.END, f"Información adicional: {info}")
            self.entrada_info.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "El campo de información está vacío.")

    def limpiar_seleccion(self):
        seleccion = self.lista_registros.curselection()
        if seleccion:
            self.lista_registros.delete(seleccion)
        else:
            messagebox.showwarning("Advertencia", "No hay ningún elemento seleccionado para borrar.")

    def limpiar_registros(self):
        self.registros.clear()
        self.lista_registros.delete(0, tk.END)

    # FUNCIONES DE TAREAS

    def añadir_tarea(self):
        tarea = self.entrada_tarea.get()
        if tarea:
            self.treeview.insert('', tk.END, values=(tarea, "Pendiente"))
            self.entrada_tarea.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingresa una tarea.")

    def marcar_completada(self):
        seleccion = self.treeview.selection()
        if seleccion:
            for item in seleccion:
                tarea, estado = self.treeview.item(item, 'values')
                if estado != "Completada":
                    self.treeview.item(item, values=(tarea, "Completada"))
                else:
                    messagebox.showwarning("Advertencia", "Esta tarea ya está completada.")
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para marcar como completada.")

    # FUNCIONES GENERALES

    def on_escape_pressed(self, event):
        messagebox.showinfo("Cerrando", "Aplicación cerrada.")
        self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionAsistencia(root)
    root.mainloop()
