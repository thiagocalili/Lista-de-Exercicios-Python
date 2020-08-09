#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#  Média de Aproveitamento  Conceito
#  Entre 9.0 e 10.0        A
#  Entre 7.5 e 9.0         B
#  Entre 6.0 e 7.5         C
#  Entre 4.0 e 6.0         D
#  Entre 4.0 e zero        E

print(''' Programa de Avaliação de Desempenho - PAD \n
Para que seja aprovado o aluno deverá obter media acima do conceito C, conforme tabela abaixo: \n
Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E \n''')

materia = str(input('Informe a matéria: '))
aluno = str(input('Informe o nome do aluno: '))

nota1 = float(input('Informe o valor da primeira nota de 0 a 10: '))
while nota1 < 0 or nota1 > 10:
        print('Valor da nota incorreto!')
        nota1 = float(input('Informe o valor da primeira nota de 0 a 10: '))

nota2 = float(input('Informe o valor da segunda nota de 0 a 10: '))
while nota2 < 0 or nota2 > 10:
    print('Valor da nota incorreto!')
    nota2 = float(input('Informe o valor da segunda nota de 0 a 10: '))
media = (nota1 + nota2) / 2

if media >= 9:
    conceito = 'A'
    situacao = 'APROVADO'
elif media >= 7.5 and media <9:
    conceito = 'B'
    situacao = 'APROVADO'
elif media >= 6 and media <7.5:
    conceito = 'C'
    situacao = 'APROVADO'
elif media >= 4 and media <6:
    conceito = 'D'
    situacao = 'REPROVADO'
else:
    conceito = 'E'
    situacao = 'REPROVADO'

print('  ')
print('###################################################################################')
print('                             BOLETIM PARCIAL BIMESTRAL                             ')
print('###################################################################################')
print('-----------------------------------------------------------------------------------')
print('ALUNO: {} '.format(aluno))
print('-----------------------------------------------------------------------------------')
print('MATÉRIA: {} '.format(materia))
print('-----------------------------------------------------------------------------------')
print('NOTA 1: {} NOTA 2: {}        MÉDIA {} '.format(nota1, nota2, media))
print('-----------------------------------------------------------------------------------')
print('CONCEITO: {}                 SITUAÇÃO ATUAL: {} '.format(conceito, situacao))
print('-----------------------------------------------------------------------------------')
print('  ')
