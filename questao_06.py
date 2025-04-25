# QUESTÃO 06:
# Leia uma string e inverta o seu conteúdo. 
# Exemplo: Se a string digitada for "JANELA", então você deve imprimir: "ALENAJ".

texto = input('Digite um texto qualquer: ')

listaChar = [char for char in texto]
listaChar.reverse()

textoInvertido = ''.join(listaChar)
print(textoInvertido)