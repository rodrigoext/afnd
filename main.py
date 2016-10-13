from afnd import AFND

def teste1():
    estados = list(['0','1'])
    alfabeto = list('ab')
    transicoes = {
        ('0', 'a') : ['1'],
        ('0', 'b') : ['0', '1'],
        ('1', 'a') : ['0'],
        ('1', 'b') : ['1']
    }
    inicial = '0'
    finais = list('0')
    afnd = AFND(estados, alfabeto, transicoes, inicial, finais)
    afnd.reconhecer('abab')
    afnd.reconhecer('aaaaabbb')

""" Seja M um automato finito nao deterministico, 
# com alfabeto binario, tal que, a entrada termine com 1
# Definicao formal M = ({p,q}, {0,1}, T, p, {q}), onde T
# eh definido por:
#    | 0 |  1  |
#   p|{p}|{p,q}|
#   q| @ |  @  |"""
def teste2():
    estados = list(['pq', 's'])
    alfabeto = list("01")
    transicoes = {
        ('pq', '0') : ['pq'],
        ('pq', '1') : ['pq', 's'],
    }
    inicial = list(['pq'])
    finais = list('s')
    afnd = AFND(estados, alfabeto, transicoes, inicial, finais)
    afnd.reconhecer('1')
    afnd.reconhecer('00')
    afnd.reconhecer('001')

if __name__ == '__main__':
    teste1()
    teste2()