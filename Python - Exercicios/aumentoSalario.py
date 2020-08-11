# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram
# para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
#baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

nome = str(input('Informe seu nome e sobrenome: '))
salario = float(input('Informe o seu salário atual: '))
if salario <= 280:
    aumento = salario * 0.2
    novoSalario = salario + aumento
    print('\n Prezado(a) {}.\n Seu salário era de R$ {}, seu aumento foi de {}%, no total de R$ {}.\n Seu novo salário passará a ser de R$ {}'.format(nome, salario, 20, aumento, novoSalario))
    print(' ')
elif salario > 280 and salario <= 700:
    aumento = salario * 0.15
    novoSalario = salario + aumento
    print('\n Prezado(a) {}.\n Seu salário era de R$ {}, seu aumento foi de {}%, no total de R$ {}.\n Seu novo salário passará a ser de R$ {}'.format(nome, salario, 15, aumento, novoSalario))
    print(' ')
elif salario > 700 and salario <= 1500:
    aumento = salario * 0.1
    novoSalario = salario + aumento
    print('\n Prezado(a) {}.\n Seu salário era de R$ {}, seu aumento foi de {}%, no total de R$ {}.\n Seu novo salário passará a ser de R$ {}'.format(nome, salario, 10, aumento, novoSalario))
    print(' ')
else:
    aumento = salario * 0.05
    novoSalario = salario + aumento
    print('\n Prezado(a) {}.\n Seu salário era de R$ {}, seu aumento foi de {}%, no total de R$ {}.\n Seu novo salário passará a ser de R$ {}'.format(nome, salario, 5, aumento, novoSalario))
    print(' ')
