from afnd import AFND

""" 
    Seja M um automato finito nao deterministico, 
    com alfabeto binario, tal que, a entrada termine com 1
    Definicao formal M = ({p,q}, {0,1}, T, p, {q}), onde T
    eh definido por:
        | 0 |  1  |
       p|{p}|{p,q}|
       q| @ |  @  |                                     """
def teste1():
    estados = list(['p', 'q'])
    alfabeto = list('01')
    transicoes = {
        ('p', '0') : ['p'],
        ('p', '1') : ['p', 'q'],
    }
    inicial = list(['p'])
    finais = list('q')
    afnd = AFND(estados, alfabeto, transicoes, inicial, finais)
    afnd.reconhecer('1')
    afnd.reconhecer('00')
    afnd.reconhecer('001')

"""
Automato para a expressao regular a* U (ab)*
"""
def teste2():
    estados = list(['q0', 'q1', 'q2', 'q3'])
    alfabeto = list('ab')
    transicoes = {
        ('q0', 'a') : ['q1', 'q2'],
        ('q1', 'a') : ['q1'],
        ('q2', 'b') : ['q3'],
        ('q3', 'a') : ['q2']
    }
    inicial = list(['q0'])
    finais = list(['q0', 'q1', 'q3'])
    afnd = AFND(estados, alfabeto, transicoes, inicial, finais)
    afnd.reconhecer('a')
    afnd.reconhecer('ab')
    afnd.reconhecer('ba')
    afnd.reconhecer('aba')
    afnd.reconhecer('abab')

"""
Automato que aceita todas as palavras onde o ultimo simbolo
eh 0 ou contem somente 1s, usando epsilon transicoes.
"""
def teste3():
    estados = list(['A', 'B', 'C', 'D'])
    alfabeto = list('01')
    transicoes = {
        ('B', '&') : ['A', 'C'],
        ('A', '1') : ['A'],
        ('C', '0') : ['C', 'D'],
        ('C', '1') : ['C']
    }
    inicial = list(['B'])
    finais = list(['A', 'D'])
    afnd = AFND(estados, alfabeto, transicoes, inicial, finais)
    afnd.reconhecer('1')
    afnd.reconhecer('111110000000')
    afnd.reconhecer('101')

"""
Automato para a expressao regular a* U (ab)*, 
usando epsilon transicoes
"""
def teste4():
    estados = list(['q0', 'q1', 'q2', 'q3', 'q4'])
    alfabeto = list('ab')
    transicoes = {
        ('q0', '&') : ['q1', 'q2'],
        ('q1', 'a') : ['q1'],
        ('q2', 'a') : ['q3'],
        ('q3', 'b') : ['q4'],
        ('q4', '&') : ['q2']
    }
    inicial = list(['q0'])
    finais = list(['q1', 'q4'])
    afnd = AFND(estados, alfabeto, transicoes, inicial, finais)
    afnd.reconhecer('a')
    afnd.reconhecer('ab')
    afnd.reconhecer('ba')
    afnd.reconhecer('aba')
    afnd.reconhecer('abab')

def teste5():
    estados = list(['q0', 'q1'])
    alfabeto = list('ab')
    transicoes = {
        ('q0', '&') : ['q1'],
        ('q1', '&') : ['q0'],
        ('q1', 'a') : ['q1']
    }
    inicial = list(['q0'])
    finais = list(['q1'])
    afnd = AFND(estados, alfabeto, transicoes, inicial, finais)
    afnd.reconhecer('a')
    afnd.reconhecer('')
    afnd.reconhecer('b')
    afnd.reconhecer('ba')

if __name__ == '__main__':
    #teste1()
    print '----'
    #teste2()
    print '----'
    #teste3()
    print '----'
    teste4()
    print '----'
    teste5()