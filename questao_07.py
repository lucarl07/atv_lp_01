# QUESTÃO 07:
# Faça um programa que leia uma string e dois caracteres. Troque todas as ocorrências do primeiro caracter pelo segundo. Exemplo: Seja a string "maracatu" e os caracteres 'a' e 'o', então a string ficará "morocotu".
# Formato de Entrada -> Você receberá 03 linhas. Primeira linha: a string; segunda linha: o primeiro caracter; terceira linha: o segundo caracter. A string possui no máximo 100 caracteres.
# Formato de Saída -> Imprima a palavra resultante da substituição dos caracteres na string original.

def substituir(string):
  charAntigo = input('Digite o caractere que deseja substituir: ')
  charNovo = input('Digite o caractere que vai substitui-lo: ')
  return string.replace(charAntigo, charNovo)

textoInicial = input('Digite o texto inicial: ')

if len(textoInicial) > 100:
  print('[ERRO] Seu texto ultrapassou 100 caracteres. Por favor, tente novamente.')
else:
  textoFinal = substituir(textoInicial)
  print(textoFinal)