
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
            estado_atual_temp = []
            for estado in list(estado_atual):
                for proximo_estado in self.transicoes[(estado, simbolo)]:
                    estado_atual_temp.append(proximo_estado)
            estado_atual = estado_atual_temp
            #print estado_atual
        aceita = [x for x in estado_atual if x in self.finais]
        if (len(aceita) > 0):
            print ''.join(['O automato RECONHECEU ', palavra])
        else:
            print ''.join(['O automato NAO RECONHECEU ', palavra])
        return len(aceita) > 0