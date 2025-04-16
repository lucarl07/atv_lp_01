# QUESTÃO 1:
# Faça um programa que leia 3 números inteiros e os imprima em ordem crescente.

inteiros = []

for _ in range(3):
  inteiros.append(int(input('-> ')))

inteiros.sort()

for i in inteiros:
  print(i)