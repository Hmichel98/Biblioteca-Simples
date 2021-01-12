import tkinter as tk
import json
from tkinter import ttk

class Botoes:

    def __init__(self, parent, entradas, tree):
        self.parent = parent
        self.entradas = entradas
        self.tree = tree

        self.style = ttk.Style()
        self.style.configure(
            "W.TButton",
            font=("Manjari Thin", 10, 'bold'),
            foreground='ghost white',
            borderwidth='3',
            background='gray10'
        )
  
        self.botao1 = tk.ttk.Button(self.parent, text='Salvar', style='W.TButton', command=lambda: [self.adicionar(), self.entradas.deletar()])
        self.botao1.place(relx=0.8, rely=0.033, anchor='center')

        self.filtrar = tk.ttk.Button(self.parent, text="Filtrar", style='W.TButton', command=self.filtrar)
        self.filtrar.place(relx=0.8, rely=0.075, anchor='center')

        self.resetar = tk.ttk.Button(self.parent, text="Resetar", style='W.TButton', command=lambda: [self.tree.deletar_tudo(), self.tree.manter_dados()])
        self.resetar.place(relx=0.8, rely=0.12, anchor='center')

    def filtrar(self):
        indexes = []
        self.nome, self.autor, self.genero = self.entradas.retornar_conteudos("nome", "autor", "genero")
        obras = self.__abrir_arquivo()
        for i in range(len(obras["nomes"])):
            if self.nome and self.autor and self.genero:
                if self.nome != obras["nomes"][i] or self.autor != obras["autores"][i] or self.genero != obras["generos"][i]:
                    indexes.append(i)
            elif self.nome and self.autor and not self.genero:
                if self.nome != obras["nomes"][i] or self.autor != obras["autores"][i]:
                    indexes.append(i)
            elif self.nome and self.genero and not self.autor:
                if self.nome != obras["nomes"][i] or self.genero != obras["generos"][i]:
                    indexes.append(i)
            elif self.autor and self.genero and not self.nome:
                if self.autor != obras["autores"][i] or self.genero != obras["generos"][i]:
                    indexes.append(i)
            elif self.nome and not self.genero and not self.autor:
                if self.nome != obras["nomes"][i]:
                    indexes.append(i)
            elif self.autor and not self.nome and not self.genero:
                if self.autor != obras["autores"][i]:
                    indexes.append(i)
            elif self.genero and not self.nome and not self.autor:
                if self.genero != obras["generos"][i]:
                    indexes.append(i)
        self.tree.tree.delete(*indexes)

    def adicionar(self):
        self.nome, self.autor, self.genero = self.entradas.retornar_conteudos("nome", "autor", "genero")
        obras = self.__abrir_arquivo()
        self.__salvar_obras(obras)
        self.tree.inserir_dados(self.nome, self.autor, self.genero)

    def __abrir_arquivo(self):
        with open("/home/usuario/Tkinter/Testando/entradas.json", 'r') as arq:
            obras = json.load(arq)
            obras["nomes"].append(self.nome)
            obras["autores"].append(self.autor)
            obras["generos"].append(self.genero)
        return obras
    
    def __salvar_obras(self, obras):
        with open("/home/usuario/Tkinter/Testando/entradas.json", 'w') as arq:
            json.dump(obras, arq)
