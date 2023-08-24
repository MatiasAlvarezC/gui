import tkinter as tk
from tkinter import ttk

class CalculadoraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")

        self.root.columnconfigure(1, weight=1)  # Añadir espacio horizontal

        self.primer_numero = tk.StringVar()
        self.segundo_numero = tk.StringVar()
        self.resultado = tk.StringVar()

        self.label_primer_numero = tk.Label(root, text="Primer número:")
        self.label_primer_numero.grid(row=0, column=0, padx=10, pady=2, sticky="w")

        self.lineedit_primer_numero = ttk.Entry(root, textvariable=self.primer_numero)
        self.lineedit_primer_numero.grid(row=0, column=1, padx=5, pady=2, sticky="e")

        self.label_segundo_numero = tk.Label(root, text="Segundo número:")
        self.label_segundo_numero.grid(row=1, column=0, padx=10, pady=2, sticky="w")

        self.lineedit_segundo_numero = ttk.Entry(root, textvariable=self.segundo_numero)
        self.lineedit_segundo_numero.grid(row=1, column=1, padx=5, pady=2, sticky="e")

        self.label_resultado = tk.Label(root, text="Resultado:")
        self.label_resultado.grid(row=2, column=0, padx=10, pady=2, sticky="w")

        self.lineedit_resultado = ttk.Entry(root, textvariable=self.resultado, state="readonly")
        self.lineedit_resultado.grid(row=2, column=1, padx=5, pady=2, sticky="e")

        self.boton_suma = tk.Button(root, text="+", command=self.sumar)
        self.boton_suma.grid(row=3, column=0, padx=10, pady=5)

        self.boton_resta = tk.Button(root, text="-", command=self.restar)
        self.boton_resta.grid(row=3, column=1, padx=10, pady=5)

        self.boton_multiplicacion = tk.Button(root, text="*", command=self.multiplicar)
        self.boton_multiplicacion.grid(row=4, column=0, padx=10, pady=5)

        self.boton_division = tk.Button(root, text="/", command=self.dividir)
        self.boton_division.grid(row=4, column=1, padx=10, pady=5)

        self.boton_modulo = tk.Button(root, text="%", command=self.modulo)
        self.boton_modulo.grid(row=5, column=0, padx=10, pady=5)

        self.boton_clear = tk.Button(root, text="CLEAR", command=self.clear)
        self.boton_clear.grid(row=5, column=1, padx=10, pady=5)

    def sumar(self):
        try:
            resultado = float(self.primer_numero.get()) + float(self.segundo_numero.get())
            self.resultado.set(str(resultado))
        except ValueError:
            self.resultado.set("Error")

    def restar(self):
        try:
            resultado = float(self.primer_numero.get()) - float(self.segundo_numero.get())
            self.resultado.set(str(resultado))
        except ValueError:
            self.resultado.set("Error")

    def multiplicar(self):
        try:
            resultado = float(self.primer_numero.get()) * float(self.segundo_numero.get())
            self.resultado.set(str(resultado))
        except ValueError:
            self.resultado.set("Error")

    def dividir(self):
        try:
            resultado = float(self.primer_numero.get()) / float(self.segundo_numero.get())
            self.resultado.set(str(resultado))
        except (ValueError, ZeroDivisionError):
            self.resultado.set("Error")

    def modulo(self):
        try:
            resultado = float(self.primer_numero.get()) % float(self.segundo_numero.get())
            self.resultado.set(str(resultado))
        except (ValueError, ZeroDivisionError):
            self.resultado.set("Error")

    def clear(self):
        self.primer_numero.set("")
        self.segundo_numero.set("")
        self.resultado.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraApp(root)
    root.geometry("250x200")
    root.mainloop()
