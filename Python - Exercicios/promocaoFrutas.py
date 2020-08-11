
#Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                      Até 5 Kg           Acima de 5 Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25.00,
#receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg)
#de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

def tipoFruta():
    fruta = int(input('Conforme a numeração acima, informe o tipo de Fruta: '))
    peso = float(input('Informe o peso total: '))
    while 1 < fruta > 3:
        print('Tipo de fruta não consta na promoção!')
        fruta = int(input('Conforme a numeração acima, informe o tipo de Fruta: '))
    
    calcPreco(fruta, peso)

def calcPreco (fruta, peso):
    if fruta == 1:
        tipo = 'Morango'
        if peso <= 5:
            totalPagar = peso * 2.5
        else:
            totalPagar = peso * 2.2
    elif fruta == 2:
        tipo = 'Maçã'
        if peso <= 5:
            totalPagar = peso * 1.8
        else:
            totalPagar = peso * 1.5
    else:
        tipo = 'Banana'
        if peso <= 5:
            totalPagar = peso * 1.4
        else:
            totalPagar = peso * 1.1
    
    if totalPagar > 25:
        totalPagar = totalPagar - totalPagar * 0.1
    
    imprimir(peso, tipo, totalPagar)


def imprimir(peso, tipo, totalPagar):
    
    print('Você comprou {} Kg de {}, totalizando R$ {} com descontos da promoção!'.format(peso, tipo, totalPagar))
    print('-------------------------------------------------------------------------------------')

print(' ')
print('-------------------------------------------------------------------------------------')
print('                                 PROMOÇÃO DE FRUTAS                                  ')
print('-------------------------------------------------------------------------------------')
print('     TIPO    |   FRUTA:     |        PROMO 1        |          PROMO 2               ')
print('-------------------------------------------------------------------------------------')
print('             |              |         Até 5 Kg      |       Acima de 5 Kg  ')
print('      1      |   Morango    |     R$ 2,50 por Kg    |      R$ 2,20 por Kg ')
print('      2      |   Maçã       |     R$ 1,80 por Kg    |      R$ 1,50 por Kg ')
print('      3      |   Banana     |     R$ 1,40 por Kg    |      R$ 1,10 por Kg ')
print('-------------------------------------------------------------------------------------')
tipoFruta()
