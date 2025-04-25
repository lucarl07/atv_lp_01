# 5. Serão dados n números correspondendo as notas da turma de alunos de uma escola. Escreva um programa que leia essas notas e calcule:
# - quantas estão mais de 10% acima da média.
# - quantas estão menos de 10% abaixo da média.
# Formato de entrada: Na primeira linha você receberá um número inteiro n, que representará a quantidade de alunos da turma. N <= 20000. Em seguida você receberá n números reais, um em cada linha, correspondendo as notas de cada aluno da turma.
# Formato de saída: Imprima na primeira linha da saída a média das notas formatada com duas casas decimais. Na segunda linha imprima quantas notas ficaram mais de 10% acima da média da turma. Na terceira linha imprima quantas notas ficaram menos de 10% abaixo da média da turma.

qtdAlunos = int(input('Digite a quantidade de alunos da turma: '))
notas = []

for N in range(qtdAlunos):
  nota = float(input(f'Digite a nota do(a) aluno(a) nº {N+1}: '))
  notas.append(nota)

mediaNotas = sum(notas) / len(notas)

# over10pct = Mais de 10 por cento (acima da média da turma)
acimaMedia_over10pct = [nota for nota in notas if nota > (mediaNotas * 1.1)]

# under10pct = Menos de 10 por cento (abaixo da média da turma)
abaixoMedia_under10pct = [nota for nota in notas if mediaNotas > nota > (mediaNotas * 0.9)]

print(f'NOTA MÉDIA DA SALA = {mediaNotas}')
print(f'NOTAS MAIS DE 10% ACIMA DA MÉDIA = {acimaMedia_over10pct}')
print(f'NOTAS MENOS DE 10% ABAIXO DA MÉDIA = {abaixoMedia_under10pct}')