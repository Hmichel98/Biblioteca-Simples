import json

class Config:

    def __init__(self):

        with open("/home/usuario/Tkinter/Testando/numero.json", 'r') as arq:
            self.numero = json.load(arq)


    def incrementar(self):
        self.numero += 1
        with open("/home/usuario/Tkinter/Testando/numero.json", 'w') as arq:
            json.dump(self.numero, arq)

        

