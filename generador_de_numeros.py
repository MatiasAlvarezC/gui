import tkinter as tk
from tkinter import ttk
import random

class GeneradorNumerosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de números")

        self.label_numero1 = tk.Label(root, text="Número 1")
        self.label_numero1.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.spin_numero1 = tk.Spinbox(root, from_=0, to=100)
        self.spin_numero1.grid(row=0, column=1, padx=10, pady=5, sticky="e")

        self.label_numero2 = tk.Label(root, text="Número 2")
        self.label_numero2.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.spin_numero2 = tk.Spinbox(root, from_=0, to=100)
        self.spin_numero2.grid(row=1, column=1, padx=10, pady=5, sticky="e")

        self.label_numero_generado = tk.Label(root, text="Número Generado:")
        self.label_numero_generado.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.lineedit_numero_generado = ttk.Entry(root, state="readonly")
        self.lineedit_numero_generado.grid(row=2, column=1, padx=10, pady=5, sticky="e")

        self.boton_generar = tk.Button(root, text="Generar", command=self.generar_numero)
        self.boton_generar.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="we")

    def generar_numero(self):
        num_min = int(self.spin_numero1.get())
        num_max = int(self.spin_numero2.get())
        numero_generado = random.randint(num_min, num_max)
        self.lineedit_numero_generado.config(state="normal")
        self.lineedit_numero_generado.delete(0, tk.END)
        self.lineedit_numero_generado.insert(0, str(numero_generado))
        self.lineedit_numero_generado.config(state="readonly")

if __name__ == "__main__":
    root = tk.Tk()
    app = GeneradorNumerosApp(root)
    root.geometry("300x200")
    root.mainloop()
