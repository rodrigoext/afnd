from afnd import AFND

if __name__ == '__main__':
    estados = list('01')
    alfabeto = list('ab')
    transicoes = {
        ('0', 'a') : '1',
        ('0', 'b') : ['0', '1'],
        #('0', 'b') : '0',
        ('1', 'a') : '0',
        ('1', 'b') : '1'
    }
    inicial = '0'
    finais = list('0')
    afnd = AFND(estados, alfabeto, transicoes, inicial, finais)
    print afnd.reconhecer('abab')
    #print afnd.reconhecer('aaaaabbb')