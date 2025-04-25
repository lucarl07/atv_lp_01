# QUESTÃO 08:
# Faça um programa para ler uma string e um caracter qualquer e calcular o índice da primeira ocorrência desse caracter na string. Caso não haja ocorrência, imprimir valor -1. 
# Exemplo: Seja a string "melancia" e o caracter 'e', então o índice da primeira ocorrência do caracter na string é 1.
# Formato de Entrada -> Você receberá duas linhas. Na primeira linha receberá uma string e na segunda linha um caracter.
# Formato de Saída -> Você deve imprimir um número inteiro correspondendo ao índice do caracter encontrado na string, seguido de um final de linha.

string = input('Digite a string: ')
caractere = input('Digite o caractere a ser encontrado: ')
print(string.find(caractere))