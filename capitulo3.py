"""#CAPITULO 3 - EX.3.3.1
def right_justify(s):
    ent_tamanho = len(s)
    print(" "*(70-(ent_tamanho+1)), s)
right_justify('teste')

print('-'*80, '\n')

#CAPITULO 3 - EX. 3.3.2
def do_twice(f, arg):
    f(arg)
    f(arg)

def print_spam(arg1):
    print(arg1)

def print_twice(arg):
    print(arg)
    print(arg)
    print('Fnção print twice')

def do_four (obj_func, arg):
    do_twice(obj_func, arg)
    do_twice(obj_func, arg)
    print ('Função do_four')


do_twice(print_twice, 'spam')
do_four(print, 'spam')

print('-'*80, '\n')
"""
#CAPITULO 3.3.3
def print_tabela():
    print_estrutura()
    print_corpo()
    print_estrutura()
    print_corpo()
    print_estrutura()

def print_estrutura():
    print("+", "-"*4, "+", "-"*4, "+")

def print_corpo():
    print("|", " "*4, "|", " "*4, "|")
    print("|", " " * 4, "|", " " * 4, "|")
    print("|", " " * 4, "|", " " * 4, "|")

print_tabela()