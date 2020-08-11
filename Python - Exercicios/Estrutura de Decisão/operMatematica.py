# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.

numero1 = float(input('Informe o valor do primeiro número: '))
numero2 = float(input('Informe o valor do segundo número: '))
operacao = int(input(''' Digite: \n 1 - Adição\n 2 - Subtração\n 3 - Multiplicação\n 4 - Divisão\n
Informe qual opeção matemática quer realizar: '''))
while 1 > operacao > 4:
    print('Valor informado incorreto!')
    operacao = int(input(''' Digite: \n 1 - Adição\n 2 - Subtração\n 3 - Multiplicação\n 4 - Divisão\n
Informe qual opeção matemática quer realizar: '''))


def operadores(operacao):
    if operacao == 1:
        tipo = 'Soma'
        fator = numero1 + numero2        
    elif operacao == 2:
        tipo = 'Subtração'
        fator = numero1 - numero2        
    elif operacao == 3:
        tipo = 'Multiplicação'
        fator = numero1 * numero2        
    else:
        tipo = 'Divisão'
        fator = numero1 / numero2    
    verificar(fator, tipo)

def verificar(fator, tipo):
    if fator%2 == 0:
        tipo1 = 'Par'
    else:
        tipo1 = 'Impar'
    if fator > 0:
        tipo2 = 'Positivo'
    else:
        tipo2 = 'Negativo'
    if fator / round(fator) == 1:
        tipo3 = 'Inteiro'
    else:
        tipo3 = ' Decimal'    
    imprimir(tipo, numero1, numero2, fator, tipo1, tipo2, tipo3)

def imprimir(tipo, numero1, numero2, fator, tipo1, tipo2, tipo3):
    print(' A {} dos números {} e {} foi de {}, um número {}, {} e {}!'.format(tipo, numero1, numero2, fator, tipo1, tipo2, tipo3))

operadores(operacao)