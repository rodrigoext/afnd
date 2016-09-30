
class AFND(object):
    def __init__(self, estados, alfabeto, transicoes, inicial, finais):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = transicoes
        self.inicial = inicial
        self.finais = finais
    
    def reconhecer(self, palavra):
        estado_atual = self.inicial
        for simbolo in palavra:
            print simbolo
        return estado_atual in self.finais