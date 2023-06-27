import tkinter as tk
from tkinter import ttk


class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Atención")
        self.geometry("800x600")

        # Crear las etiquetas para indicar el tipo de atención
        estilo_etiqueta = ttk.Style()
        estilo_etiqueta.configure(
            "EstiloEtiqueta.TLabel", font=("Arial", 14, "bold"))
        self.etiqueta_caja = ttk.Label(
            self, text="Caja", style="EstiloEtiqueta.TLabel")
        self.etiqueta_caja.place(x=600, y=20)

        self.etiqueta_atencion = ttk.Label(
            self, text="Atención", style="EstiloEtiqueta.TLabel")
        self.etiqueta_atencion.place(x=200, y=20)

        # Crear las listas de atención
        self.lista_caja = tk.Listbox(self)
        self.lista_caja.place(x=600, y=50)
        self.lista_caja.configure(font=("Arial", 12))

        self.lista_atencion = tk.Listbox(self)
        self.lista_atencion.place(x=200, y=50)
        self.lista_atencion.configure(font=("Arial", 12))

        # Crear el botón "Nueva Atención" con estilo
        estilo_boton = ttk.Style()
        estilo_boton.configure("EstiloBoton.TButton", font=(
            "Arial", 12), foreground="white", background="#007bff")
        self.boton_nueva_atencion = ttk.Button(
            self, text="Nueva Atención", style="EstiloBoton.TButton", command=self.abrir_formulario)
        self.boton_nueva_atencion.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

        self.contador_caja = 1  # Variable contador para la lista de caja
        self.contador_atencion = 1  # Variable contador para la lista de atención

        # Llamar a la función verificar_listas cada 3 segundos
        self.after(30000, self.verificar_listas)

    def verificar_listas(self):
        if self.lista_caja.size() > self.lista_atencion.size():
            # Eliminar el primer ítem de la lista de caja
            self.lista_caja.delete(0)
        elif self.lista_atencion.size() > self.lista_caja.size():
            # Eliminar el primer ítem de la lista de atención
            self.lista_atencion.delete(0)

        # Llamar a la función verificar_listas nuevamente después de 3 segundos
        self.after(20000, self.verificar_listas)

    def abrir_formulario(self):
        formulario = Formulario(self)
        self.wait_window(formulario)


class Formulario(tk.Toplevel):
    def __init__(self, ventana_principal):
        super().__init__(ventana_principal)
        self.ventana_principal = ventana_principal  # Referencia a la ventana principal
        self.title("Nueva Atención")
        self.geometry("400x300")

        # Crear el contenedor principal con estilo
        estilo_contenedor = ttk.Style()
        estilo_contenedor.configure(
            "EstiloContenedor.TFrame", background="#f0f0f0")
        contenedor = ttk.Frame(self, style="EstiloContenedor.TFrame")
        contenedor.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Crear los campos del formulario con estilo
        estilo_etiqueta = ttk.Style()
        estilo_etiqueta.configure(
            "EstiloEtiqueta.TLabel", background="#f0f0f0", font=("Arial", 12))
        estilo_entry = ttk.Style()
        estilo_entry.configure("EstiloEntry.TEntry",
                               background="white", font=("Arial", 12))

        numero_documento_label = ttk.Label(
            contenedor, text="Número de Documento:", style="EstiloEtiqueta.TLabel")
        numero_documento_label.grid(
            row=0, column=0, padx=10, pady=10, sticky="w")

        self.numero_documento_entry = ttk.Entry(
            contenedor, style="EstiloEntry.TEntry")
        self.numero_documento_entry.grid(row=0, column=1, padx=10, pady=10)

        nombre_label = ttk.Label(
            contenedor, text="Nombre:", style="EstiloEtiqueta.TLabel")
        nombre_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.nombre_entry = ttk.Entry(contenedor, style="EstiloEntry.TEntry")
        self.nombre_entry.grid(row=1, column=1, padx=10, pady=10)

        tipo_atencion_label = ttk.Label(
            contenedor, text="Tipo de Atención:", style="EstiloEtiqueta.TLabel")
        tipo_atencion_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.tipo_atencion_combobox = ttk.Combobox(
            contenedor, values=["Caja", "Atención"], style="TCombobox")
        self.tipo_atencion_combobox.grid(row=2, column=1, padx=10, pady=10)

        # Crear el botón "Guardar" con estilo
        estilo_boton = ttk.Style()
        estilo_boton.configure("EstiloBoton.TButton", font=(
            "Arial", 12), foreground="white", background="#007bff")
        boton_guardar = ttk.Button(
            contenedor, text="Guardar", style="EstiloBoton.TButton", command=self.guardar_cliente)
        boton_guardar.grid(row=3, columnspan=2, padx=10, pady=10)

    def guardar_cliente(self):
        numero_documento = self.numero_documento_entry.get()
        nombre = self.nombre_entry.get()
        tipo_atencion = self.tipo_atencion_combobox.get()

        if tipo_atencion == "Caja":
            identificacion = f"CA{self.ventana_principal.contador_caja}"
            self.ventana_principal.lista_caja.insert(
                tk.END, f"{identificacion} - {nombre}")
            self.ventana_principal.contador_caja += 1
        elif tipo_atencion == "Atención":
            identificacion = f"AT{self.ventana_principal.contador_atencion}"
            self.ventana_principal.lista_atencion.insert(
                tk.END, f"{identificacion} - {nombre}")
            self.ventana_principal.contador_atencion += 1

        self.destroy()


if __name__ == "__main__":
    ventana = VentanaPrincipal()
    ventana.mainloop()
