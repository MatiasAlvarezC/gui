import tkinter as tk
from tkinter import ttk

class PeliculasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Películas")

        self.label_titulo = tk.Label(root, text="Escribe el título de una película")
        self.label_titulo.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.lineedit_pelicula = ttk.Entry(root)
        self.lineedit_pelicula.grid(row=1, column=0, padx=20, pady=5, sticky="w")

        self.boton_anadir = tk.Button(root, text="Añadir", command=self.anadir_pelicula)
        self.boton_anadir.grid(row=2, column=0, padx=45, pady=5, sticky="w")

        self.label_peliculas = tk.Label(root, text="        Películas")
        self.label_peliculas.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        self.list_widget = tk.Listbox(root)
        self.list_widget.grid(row=1, column=1, rowspan=2, padx=10, pady=5, sticky="e")

    def anadir_pelicula(self):
        pelicula = self.lineedit_pelicula.get()
        if pelicula:
            self.list_widget.insert(tk.END, pelicula)
            self.lineedit_pelicula.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = PeliculasApp(root)
    root.geometry("400x300")
    root.mainloop()

