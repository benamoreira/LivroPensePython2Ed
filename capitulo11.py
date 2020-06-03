fin = open('words.txt')

def cria_dicionario(fin):
    dicionario = dict()
    valor = 0
    for palavra in fin:
        if palavra not in dicionario:
            dicionario[valor].append(palavra)
        else:
            return
cria_dicionario(fin)