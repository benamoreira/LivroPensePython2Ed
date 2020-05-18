def rotate_word(palavra1, num):
    print(palavra1, num)
    CARACTERES = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    decifrada = ''
    for l in palavra1:
        if l in CARACTERES:
            num = CARACTERES.find(l)
            print('variavel lista: ', num)
            decifrada = decifrada + CARACTERES[valor]
            print('Decifrada: ', decifrada)

palavra1 = input('Digite a palavra: ').upper()
valor = int(input('Digite a quantidade de rotação: '))
rotate_word(palavra1, valor)


print('\nCONTA CARACTERES')
palavra = 'banana'
print(palavra.count('n'))