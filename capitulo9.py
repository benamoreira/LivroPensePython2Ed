fin = open('words.txt')
print('VERIFICA SE TEM "E"')

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

print('PALAVRAS COM + DE 20 CARACTERES')
for line in fin:
    if len(line) > 20:
        print(line)