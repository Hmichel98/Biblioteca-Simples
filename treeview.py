import tkinter as tk
from tkinter import ttk
import json

class Arvore:

    def __init__(self, parent, config):
        self.parent = parent
        self.config = config

        self.style = ttk.Style()
        self.style.theme_use("default")
        self.style.configure("Treeview",
                background='mint cream',
                foreground='gray0',
                rowheight=25,
                fieldbackground='mint cream')
        self.style.map('Treeview',
                background=[('selected', 'black')])
        self.style.configure("Treeview.Heading", font=("Manjari Bold", 12))

        self.tree = ttk.Treeview(self.parent, height=25)

        self.tree['columns'] = ("nome", "autor", "genero")

        self.tree.column("#0", width=0, stretch="no")
        self.tree.column("nome", anchor='w', width=225)
        self.tree.column("autor", anchor='center', width=175)
        self.tree.column("genero", anchor='e', width=175)

        self.tree.heading("#0", text='', anchor='w')
        self.tree.heading("nome", text="Nome", anchor='w')
        self.tree.heading("autor", text="Autor", anchor='center')
        self.tree.heading("genero", text="Gênero", anchor='e')

        self.tree.place(relx=0.5, rely=0.55, anchor="center")

        self.manter_dados()

    def inserir_dados(self, obra, autor, genero):
        self.tree.insert(parent='', index="end", iid=self.config.numero, text="", values=(obra, autor, genero))
        self.config.incrementar()

    def manter_dados(self):
        with open("/home/usuario/Tkinter/Testando/entradas.json") as arq:
            obras = json.load(arq)
        
        for i in range(len(obras["nomes"])):
            self.tree.insert(parent='', index='end', iid=i, text='', values=(obras["nomes"][i], obras["autores"][i], obras["generos"][i]))
       



    def deletar_tudo(self):
        self.tree.delete(*self.tree.get_children())