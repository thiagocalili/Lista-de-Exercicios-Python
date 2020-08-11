# Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
# Dica: utilize uma função de arredondamento.
print(' ')
numero = float(input('Digite um número: '))
if numero / round(numero) == 1:
    print('O número digitado é INTEIRO')
else:
    print('O número digitado é DECIMAL')
print(' ')