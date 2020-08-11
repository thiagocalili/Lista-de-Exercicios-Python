#O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                      Até 5 Kg           Acima de 5 Kg
#File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
#porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara
#o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o
#tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações
#da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.


def imprimir(peso, tipo, totalPagar, pagamento, tipoPag):
    
    print('Você comprou {} Kg de {}, pagamento em {}, totalizando R$ {} com descontos da promoção!'.format(peso, tipo, tipoPag, totalPagar))
    print('-------------------------------------------------------------------------------------')
    print(' ')

def inicioCompra():
    carne = int(input('Conforme a numeração acima, informe o tipo de Carne: '))
    peso = float(input('Informe o peso total: '))
    while 1 < carne > 3:
        print('Tipo de carne não consta na promoção!')
        carne = int(input('Conforme a numeração acima, informe o tipo de Carne: '))
    pagamento = int(input('Informe a forma de pagamento: '))
    
    if pagamento == 1:
        tipoPag = 'Dinheiro'
    elif pagamento == 2:
        tipoPag = 'Débito'
    elif pagamento == 3:
        tipoPag = 'Crédito'
    else:
        tipoPag = 'Cartão Tabajara'
    
    calcPreco(carne, peso, pagamento, tipoPag)

def calcPreco (carne, peso, pagamento, tipoPag):
    if carne == 1:
        tipo = 'CONTRA-FILÉ'
        if peso <= 5:
            totalPagar = peso * 12.5
        else:
            totalPagar = peso * 11.2
    elif carne == 2:
        tipo = 'ALCATRA'
        if peso <= 5:
            totalPagar = peso * 20.3
        else:
            totalPagar = peso * 19.1
    else:
        tipo = 'PICANHA'
        if peso <= 5:
            totalPagar = peso * 31.4
        else:
            totalPagar = peso * 29.9
    
    if pagamento == 4:
        totalPagar = totalPagar - totalPagar * 0.05
    
    imprimir(peso, tipo, totalPagar, pagamento, tipoPag)

print(' ')
print('-----------------------------------------------------------------------------------')
print('                                 PROMOÇÃO DE CARNES                                ')
print('-----------------------------------------------------------------------------------')
print('     TIPO    |   CARNE:     |        PROMO 1        |          PROMO 2             ')
print('-----------------------------------------------------------------------------------')
print('             |              |         Até 5 Kg      |       Acima de 5 Kg  ')
print('      1      |  CONTRA-FILÉ |    R$ 12,50 por Kg    |      R$ 11,20 por Kg ')
print('      2      |   ALCATRA    |    R$ 20,30 por Kg    |      R$ 19,10 por Kg ')
print('      3      |   PICHANHA   |    R$ 31,40 por Kg    |      R$ 29,90 por Kg ')
print('-----------------------------------------------------------------------------------')
print('TIPO PAGAMENTO: 1 - DINHEIRO / 2 - DEBITO / 3 - CREDITO / 4 - CARTÃO TABAJARA ')
print('-----------------------------------------------------------------------------------')

inicioCompra()