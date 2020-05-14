def eval_loop(entrada):
    while True:
        print(eval(entrada))
        opcao = input('Fechar? ').lower()
        if opcao != 'fechar':
            entrada = input('Digite uma entrada: ')
        else:
            print('Finalizado')
            break

entrada = input('Digite uma entrada: ')
eval_loop(entrada)

def mysquart(valor, estimativa):
    while True:
        print(estimativa)
        y = (estimativa + valor/estimativa) / 2
        if y == estimativa:
            break
        estimativa = y

valor = int(input('Digite o numero: '))
estimativa = int(input('Digite a estimativa: '))
mysquart(valor, estimativa)