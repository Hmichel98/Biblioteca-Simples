import tkinter as tk
from botao import Botoes
from entradas import Entradas
from treeview import Arvore
from config import Config
from tkinter import ttk

class MainApplication(tk.Frame):

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.parent.configure(background='black')
        self.config = Config()

        self.tree = Arvore(self.parent, self.config)
        self.entradas = Entradas(self.parent)
        self.botoes = Botoes(self.parent, self.entradas, self.tree)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('650x800')
    root.title("Biblioteca")
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()