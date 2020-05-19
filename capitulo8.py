def rotate_word(palavra1, valor):
    CARACTERES = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    decifrada = ''
    for letra in palavra1:
        if letra in CARACTERES:
            num = CARACTERES.find(letra)
            num = num + valor
            decifrada = decifrada + CARACTERES[num]
    print('palavra decifrada: ', decifrada)

palavra1 = input('Digite a palavra: ').upper()
valor = int(input('Digite a quantidade de rotação: '))
rotate_word(palavra1, valor)



print('\nCONTA CARACTERES')
palavra = 'banana'
print(palavra.count('n'))