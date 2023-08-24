import tkinter as tk
from tkinter import ttk

class ContadorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Factorial")

        self.contador = 1

        self.label_contador = tk.Label(root, text="n:")
        self.label_contador.grid(row=0, column=0)

        self.valor_lineedit = ttk.Entry(root, state="readonly", font=("Arial", 16))
        self.valor_lineedit.grid(row=0, column=1, padx=20, pady=10)
        self.actualizar_valor()

        self.label_factorial = tk.Label(root, text="Factorial (n):")
        self.label_factorial.grid(row=0, column=2)

        self.factorial_lineedit = ttk.Entry(root, state="readonly", font=("Arial", 16))
        self.factorial_lineedit.grid(row=0, column=3, padx=20, pady=10)
        self.actualizar_factorial()

        self.boton_siguiente = tk.Button(root, text="Siguiente", command=self.siguiente)
        self.boton_siguiente.grid(row=0, column=4, padx=10, pady=10)

    def actualizar_valor(self):
        self.valor_lineedit.config(state="normal")
        self.valor_lineedit.delete(0, tk.END)
        self.valor_lineedit.insert(0, str(self.contador))
        self.valor_lineedit.config(state="readonly")

    def actualizar_factorial(self):
        factorial = 1
        for i in range(1, self.contador + 1):
            factorial *= i
        self.factorial_lineedit.config(state="normal")
        self.factorial_lineedit.delete(0, tk.END)
        self.factorial_lineedit.insert(0, str(factorial))
        self.factorial_lineedit.config(state="readonly")

    def siguiente(self):
        self.contador += 1
        self.actualizar_valor()
        self.actualizar_factorial()

if __name__ == "__main__":
    root = tk.Tk()
    app = ContadorApp(root)
    root.geometry("800x100")
    root.mainloop()
