
class AFND(object):
    def __init__(self, estados, alfabeto, transicoes, inicial, finais):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = transicoes
        self.inicial = inicial
        self.finais = finais
    
    def reconhecer(self, palavra):
        estado_atual = self.inicial
        
        if (self.inicial[0], '&') in self.transicoes:
            estado_atual = self.transicoes[(self.inicial[0], '&')]
        
        for simbolo in palavra:
            aux = estado_atual
            for estado in list(estado_atual):
                if (estado, '&') in self.transicoes:
                    epsilon_transicoes = self.transicoes[(estado, '&')]
                    aux = list(set().union(aux, epsilon_transicoes))
            estado_atual = aux
            print estado_atual
            aux = []
            for estado in list(estado_atual):
                if (estado, simbolo) in self.transicoes:
                    proximos_estados = self.transicoes[(estado, simbolo)]
                    for proximo_estado in self.transicoes[(estado, simbolo)]:
                        aux.append(proximo_estado)
            estado_atual = aux
        aceita = [x for x in estado_atual if x in self.finais]
        
        if (len(aceita) > 0):
            print ''.join(['O automato RECONHECEU       ', palavra])
        else:
            print ''.join(['O automato NAO RECONHECEU   ', palavra])
        return len(aceita) > 0