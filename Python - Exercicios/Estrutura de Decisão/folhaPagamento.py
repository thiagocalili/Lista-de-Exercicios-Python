#  Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
#  que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde
#  a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde
#  ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade
#  de horas trabalhadas no mês.
#   Desconto do IR:
#   Salário Bruto até 900 (inclusive) - isento
#   Salário Bruto até 1500 (inclusive) - desconto de 5%
#   Salário Bruto até 2500 (inclusive) - desconto de 10%
#   Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo
#   abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#
#   Salário Bruto: (5 * 220)        : R$ 1100,00
#        (-) IR (5%)                     : R$   55,00  
#        (-) INSS ( 10%)                 : R$  110,00
#        FGTS (11%)                      : R$  121,00
#        Total de descontos              : R$  165,00
#        Salário Liquido                 : R$  935,00

nome = str(input('Informe o nome completo do funcionário:'))
valorHora = float(input(' Informe o valor do salário por hora: '))
horasTrabalhadas = float(input('Informe as horas trabalhadas no mês: '))
salarioBruto = (valorHora * horasTrabalhadas)

def calculoDescontos(salarioBruto):
    descontoIR = 0
    inss = salarioBruto * 0.10
    fgts = salarioBruto * 0.11
    sindicato = salarioBruto * 0.03
    impostoIR = 0
    if salarioBruto <= 900:
        descontoIR = 'Isento'
        totalDesconto = sindicato + inss
        salarioLiquido = salarioBruto - totalDesconto
    elif salarioBruto > 900 and salarioBruto <= 1500:
        impostoIR = 5
        descontoIR = salarioBruto * 0.05
        totalDesconto = sindicato + inss + descontoIR + impostoIR
        salarioLiquido = salarioBruto - totalDesconto
    elif salarioBruto > 1500 and salarioBruto <= 2500:
        impostoIR = 10
        descontoIR = salarioBruto * 0.1
        totalDesconto = sindicato + inss + descontoIR + impostoIR
        salarioLiquido = salarioBruto - totalDesconto
    else:
        impostoIR = 20        
        descontoIR = salarioBruto * 0.2
        totalDesconto = sindicato + inss + descontoIR + impostoIR
        salarioLiquido = salarioBruto - totalDesconto

    imprimir(salarioBruto, sindicato, descontoIR, totalDesconto, fgts, salarioLiquido, impostoIR, inss)

def imprimir(salarioBruto, sindicato, descontoIR, totalDesconto, fgts, salarioLiquido, impostoIR, inss):
    print('  ')
    print('###################################################################################')
    print('                              EXTRATO BASE DE SALÁRIO                              ')
    print('###################################################################################')
    print('-----------------------------------------------------------------------------------')
    print('Funcionário: {} '.format(nome))
    print('-----------------------------------------------------------------------------------')
    print('                     Salário Bruto: ({} * {})        : R$ {} '.format(valorHora, horasTrabalhadas, salarioBruto))
    print('-----------------------------------------------------------------------------------')
    print('    (-) IR ({}%)                    : R$  {} '.format(impostoIR, descontoIR))
    print('    (-) INSS ( 10%)                 : R$  {} '.format(inss))
    print('    (-) SINDICATO ( 3%)             : R$  {} '.format(sindicato))
    print('    FGTS (11%)                      : R$  {} '.format(fgts))
    print('    Total de descontos              : R$  {} '.format(totalDesconto))
    print('-----------------------------------------------------------------------------------')
    print('                                     Salário Liquido                 : R$  {}  '.format(salarioLiquido))
    print('-----------------------------------------------------------------------------------')
    print('  ')
calculoDescontos(salarioBruto)
