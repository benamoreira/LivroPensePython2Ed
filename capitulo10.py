print('CAP 10 - Ex 10.5')
lista_ex_5 = [1,4,3]
def is_sorted(lista_ex_5):
    return lista_ex_5 == sorted(lista_ex_5)
print(is_sorted(lista_ex_5))

print('CAP 10 - Ex 10.4')
lista_ex_3 = [1, 2, 3, 4]
def chop(lista_ex_3):
    del lista_ex_3[0]
    del lista_ex_3[-1]
print('Lista 4: ', chop(lista_ex_3))


print('CAP 10 - Ex 10.3')
def midlle(lista_ex_3):
    res = []
    tamanho = len(lista_ex_3)
    res = lista_ex_3[1:tamanho-1]
    return res

print('Resultado Exercício 3: ', midlle(lista_ex_3))


print('CAP 10 - Ex 10.2')
lista_ex_2 = [1, 2, 10]

def cumsum(lista_ex_2):
    total = 0
    res = []
    for e in lista_ex_2:
        total += e
        print(e)
        res.append(total)
    return res
print('Resultado: ', cumsum(lista_ex_2))

print('\nCAP 10 - Ex 10.1')
lista1 = [9,2]
lista2 = [4,5,6]
lista3 = [3]
lista_inteiros = lista1 + lista2 + lista3

def nested_sum(lista_inteiros):
    res = []
    res = sorted(lista_inteiros)
    return res

print(nested_sum(lista_inteiros))