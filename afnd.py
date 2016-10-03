
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
            #if isinstance(estado_atual, list):
            estado_atual_temp = []
            for estado in list(estado_atual):
                proximos_estados = list(self.transicoes[(estado, simbolo)])
                for proximo_estado in proximos_estados:
                    estado_atual_temp.append(proximo_estado)
            estado_atual = estado_atual_temp
            print estado_atual
        #return estado_atual in self.finais
        aceita = [x for x in estado_atual if x in self.finais]
        return len(aceita) > 0