# QUESTÃO 04: 
# Faça um programa que dado um número indique se ele é um primo ou não.
# Obs: Para cada número lido você deve imprimir “Número não é Primo” caso o número não seja primo ou “Número Primo” caso seja.

numero = int(input('Digite um número a ser analisado: '))

isPrimo = True

for i in range(numero):
  for j in range(numero):
    if i * j == numero:
      isPrimo = False

if isPrimo == True:
  print('Número Primo')
else:
  print('Número não é Primo')