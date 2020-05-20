fin = open('words.txt')

def avoids(palavra2, proibidas):
    for l in palavra2:
        if l in proibidas:
            return False
    return True

def uses_only(palavra2, disponiveis):
    for l in palavra2:
        if l not in disponiveis:
            return False
    return True

palavra2 = str(input('Digite uma palavra: '))
proibidas = input('Letras proibidas: ')
disponiveis = input('Letras disponíveis: ')
avoids(palavra2, proibidas)




print('9.2 - VERIFICA SE TEM "E"')

def has_no_e(fin):
    total_linhas = 0
    total_true = 0
    letra = 'e'
    print('TOTAIS ZERADoS', total_linhas, total_true)
    for linha in fin:
        if not letra in linha:
            print('Não tem E = True')
            total_true += 1
        total_linhas += 1
    print('Total de Palavras:', total_linhas)
    print(total_true, '- Não tem "E" na palavra.\n')

    porcentagem = (total_true / total_linhas) * 100
    print('{:2} não contem "E"'.format(porcentagem))

has_no_e(fin)

print('9.1 - PALAVRAS COM + DE 20 CARACTERES')
for line in fin:
    if len(line) > 20:
        print(line)