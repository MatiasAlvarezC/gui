import tkinter as tk
from tkinter import ttk

class ContadorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ContDecreciente")

        self.contador = 88

        self.label = tk.Label(root, text="Contador:")
        self.label.grid(row=0, column=0)

        self.valor_lineedit = ttk.Entry(root, state="readonly", font=("Arial", 16))
        self.valor_lineedit.grid(row=0, column=1, padx=20, pady=10)
        self.actualizar_valor()

        self.boton_decrementar = tk.Button(root, text="-", command=self.decrementar)
        self.boton_decrementar.grid(row=0, column=2)

    def actualizar_valor(self):
        self.valor_lineedit.config(state="normal")
        self.valor_lineedit.delete(0, tk.END)
        self.valor_lineedit.insert(0, str(self.contador))
        self.valor_lineedit.config(state="readonly")

    def decrementar(self):
        self.contador -= 1
        self.actualizar_valor()

if __name__ == "__main__":
    root = tk.Tk()
    app = ContadorApp(root)
    root.geometry("400x100")
    root.mainloop()
