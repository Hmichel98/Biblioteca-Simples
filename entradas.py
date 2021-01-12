import tkinter as tk
from tkinter import ttk

class Entradas:

    def __init__(self, parent):
        self.parent = parent

        self.style_label = ttk.Style()
        self.style_label.configure(
            "TLabel",
            foreground='gray10',
            font=("Manjari Bold", 15)
        )

        self.style_entry = ttk.Style()
        self.style_entry.configure(
            "TEntry",
            background='black',
            foreground='gray10'
        )


        tk.ttk.Label(self.parent, text="Nome:", style='TLabel').place(relx=0.1, rely=0.033, anchor='center')
        self.nome = tk.ttk.Entry(self.parent, style='TEntry', font=("Manjari Bold", 17))
        self.nome.place(relx=0.35, rely=0.033, anchor='center')

        tk.ttk.Label(self.parent, text="Autor:", style='TLabel').place(relx=0.1, rely=0.075, anchor='center')
        self.autor = tk.ttk.Entry(self.parent, style='TEntry', font=("Manjari Bold", 17))
        self.autor.place(relx=0.35, rely=0.075, anchor='center')

        tk.ttk.Label(self.parent, text="Gênero:", style='TLabel').place(relx=0.1, rely=0.12, anchor='center')
        self.genero = tk.ttk.Entry(self.parent, style='TEntry', font=("Manjari Bold", 17))
        self.genero.place(relx=0.35, rely=0.12, anchor='center')

    def retornar_conteudos(self, *chaves):
        obras = []
        for chave in chaves:
            obras.append(self.retornar_all_gets()[chave])
        return obras

    def retornar_all_gets(self):
        todos_gets = {"nome": self.nome.get(), "autor": self.autor.get(), "genero": self.genero.get()}
        return todos_gets

    def deletar(self):
        self.nome.delete(0, 'end')
        self.autor.delete(0, 'end')
        self.genero.delete(0, 'end')