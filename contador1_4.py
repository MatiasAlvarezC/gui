import tkinter as tk
from tkinter import ttk

class ContadorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contador")

        self.contador = 0

        self.label = tk.Label(root, text="Contador:")
        self.label.grid(row=0, column=0)

        self.valor_lineedit = ttk.Entry(root, state="readonly", font=("Arial", 16))
        self.valor_lineedit.grid(row=0, column=1, padx=20, pady=10)
        self.actualizar_valor()

        self.boton_count_up = tk.Button(root, text="Count Up", command=self.count_up)
        self.boton_count_up.grid(row=0, column=2, padx=10)

        self.boton_count_down = tk.Button(root, text="Count Down", command=self.count_down)
        self.boton_count_down.grid(row=0, column=3, padx=10)

        self.boton_reset = tk.Button(root, text="Reset", command=self.reset)
        self.boton_reset.grid(row=0, column=4, padx=10)

    def actualizar_valor(self):
        self.valor_lineedit.config(state="normal")
        self.valor_lineedit.delete(0, tk.END)
        self.valor_lineedit.insert(0, str(self.contador))
        self.valor_lineedit.config(state="readonly")

    def count_up(self):
        self.contador += 1
        self.actualizar_valor()

    def count_down(self):
        self.contador -= 1
        self.actualizar_valor()

    def reset(self):
        self.contador = 0
        self.actualizar_valor()

if __name__ == "__main__":
    root = tk.Tk()
    app = ContadorApp(root)
    root.geometry("600x100")
    root.mainloop()
