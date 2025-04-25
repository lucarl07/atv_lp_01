# QUESTÃO 09:
# Escreva um programa leia 2 valores X e Y e que imprima todos os valores entre eles cujo resto da divisão dele por 5 for igual a 2 ou igual a 3.
# Formato de Entrada -> Contém 2 valores inteiros quaisquer, não necessariamente em ordem crescente.
# Formato de Saída -> Todos os inteiros entre x e y, um por linha.

print('Digite abaixo dois números, pulando uma linha (aperte a tecla Enter) para cada um deles:')
X = int(input('-> '))
Y = int(input('-> '))

valores = []

if X > Y: 
  passo = -1
else: 
  passo = 1

for i in range(X, Y, passo):
  if i % 5 == 2 or i % 5 == 3:
    valores.append(i)

print('=:=:= LISTA DE VALORES =:=:=')
for n in valores: print(f'{n} \n')