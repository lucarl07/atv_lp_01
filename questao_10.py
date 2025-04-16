# QUESTÃO 10:
# Faça um programa que leia n números inteiros dados e os imprima:
# a) na ordem inversa dos números dados
# b) ordenado em ordem decrescente

numeros = []
Q = int(input('Digite quantos números gostaria de ler: '))

print('Agora, digite abaixo números inteiros: ')

for _ in range(Q):
  numeros.append(int(input('-> ')))

# Números ordenados no inverso da lista:
i = -1
invNumeros = []

while abs(i) <= len(numeros):
  invNumeros.append(numeros[i])
  i -= 1

print(f'Lista de números em ordem invertida: {invNumeros}')

# Números ordenados em ordem decrescente:
decNumeros = numeros
decNumeros.sort(reverse=True)

print(f'Lista de números em ordem decrescente: {decNumeros}')