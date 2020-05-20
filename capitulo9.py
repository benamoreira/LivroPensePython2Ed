fin = open('words.txt')

def avoids(palavra2, proibidas):
    c = 0
    length = len(palavra2)
    for l in palavra2:
        for c in proibidas:
            if not c in palavra2:
                return print(True)
            else:
                return print(c)
            break


palavra2 = str(input('Digite uma palavra: '))
proibidas = input('Letras proibidas: ')
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