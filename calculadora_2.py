import tkinter as tk
from tkinter import ttk

class CalculadoraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora 2")

        self.label_valor1 = tk.Label(root, text="Valor 1:")
        self.label_valor1.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.valor1 = tk.StringVar()
        self.lineedit_valor1 = ttk.Entry(root, textvariable=self.valor1)
        self.lineedit_valor1.grid(row=0, column=1, padx=10, pady=5, sticky="e")

        self.label_valor2 = tk.Label(root, text="Valor 2:")
        self.label_valor2.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.valor2 = tk.StringVar()
        self.lineedit_valor2 = ttk.Entry(root, textvariable=self.valor2)
        self.lineedit_valor2.grid(row=1, column=1, padx=10, pady=5, sticky="e")

        self.label_operaciones = tk.Label(root, text="Operaciones:")
        self.label_operaciones.grid(row=0, column=2, padx=10, pady=5, sticky="w")

        self.operacion = tk.StringVar(value="Sumar")
        self.radiobutton_sumar = tk.Radiobutton(root, text="Sumar", variable=self.operacion, value="Sumar")
        self.radiobutton_sumar.grid(row=1, column=2, padx=10, pady=5, sticky="w")

        self.radiobutton_restar = tk.Radiobutton(root, text="Restar", variable=self.operacion, value="Restar")
        self.radiobutton_restar.grid(row=2, column=2, padx=10, pady=5, sticky="w")

        self.radiobutton_multiplicar = tk.Radiobutton(root, text="Multiplicar", variable=self.operacion, value="Multiplicar")
        self.radiobutton_multiplicar.grid(row=3, column=2, padx=10, pady=5, sticky="w")

        self.radiobutton_dividir = tk.Radiobutton(root, text="Dividir", variable=self.operacion, value="Dividir")
        self.radiobutton_dividir.grid(row=4, column=2, padx=10, pady=5, sticky="w")

        self.label_resultado = tk.Label(root, text="Resultado:")
        self.label_resultado.grid(row=5, column=0, padx=10, pady=5, sticky="w")

        self.resultado = tk.StringVar()
        self.lineedit_resultado = ttk.Entry(root, textvariable=self.resultado, state="readonly")
        self.lineedit_resultado.grid(row=5, column=1, padx=10, pady=5, sticky="e")

        self.boton_calcular = tk.Button(root, text="Calcular", command=self.calcular)
        self.boton_calcular.grid(row=6, column=0, columnspan=3, padx=10, pady=10, sticky="we")

    def calcular(self):
        valor1 = float(self.valor1.get())
        valor2 = float(self.valor2.get())
        operacion = self.operacion.get()

        if operacion == "Sumar":
            resultado = valor1 + valor2
        elif operacion == "Restar":
            resultado = valor1 - valor2
        elif operacion == "Multiplicar":
            resultado = valor1 * valor2
        elif operacion == "Dividir":
            resultado = valor1 / valor2

        self.resultado.set(resultado)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraApp(root)
    root.geometry("350x300")
    root.mainloop()
