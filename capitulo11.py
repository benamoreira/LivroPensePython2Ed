fin = open('words.txt')

def cria_dicionario(fin):
    dicionario = dict()
    for linha in fin:
        palavra = linha.strip().lower()
        dicionario[palavra] = palavra
    return dicionario

cria_dicionario(fin)