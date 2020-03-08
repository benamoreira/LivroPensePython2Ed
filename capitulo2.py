print('Capitulo 2 - Ex. 2.2.1')
r = 5
pi = 3.14
volume = (4/3)*pi*(r**3)
print(volume)

print('\nCap 2 - Exercicio 2.2.2')
preco_capa = 24.95
desc = 60/100
transporte= 3
outros_transportes = 75/100
primeiro_livro = (preco_capa * desc) + transporte
outros_livros = ((preco_capa * desc) + outros_transportes) * 59
print('O preço do 1 Livro sai por R$', primeiro_livro)
print('Os outros 59 livros saem por: R$', outros_livros)
print('O Total gastos em 60 livros é de: R$', primeiro_livro + outros_livros)

print('\n CAP 2 - EXERCÍCIO - 2.2.3')
primeiro_km = (8 * 60) + 15
proximos_km = ((7*60) + 12) * 3
ultimo_km = primeiro_km
total_percorrido_segundos = (primeiro_km + proximos_km + ultimo_km)
total_hora_dia = ((6*60) + 52)*60
soma_saida_percurso = total_percorrido_segundos + total_hora_dia
hora_chegada = (soma_saida_percurso//60)//60
min_chegada = (soma_saida_percurso//60) % 60
seg_chegada = (soma_saida_percurso % 60)

print(soma_saida_percurso)
print('Chega em casa às:', hora_chegada, 'h', min_chegada, 'm', seg_chegada, 's')


#6h52m00s + 08m15s = 7h00m15s
#7h00m15s + 21m36s = 7h21m51s
#7h21m51s + 08m15s = 7h30m06s











