#Calcular as duas raízes na fórmula de Báskara.
print('Vamos calcular as raízes na fórmula de Báskara.')
#import math
a=(float(input('Informe o valor de a: ')))
b=(float(input('Informe o valor de b: ')))
c=(float(input('Informe o valor de c: ')))
delta=((b*b)-4*a*c)

print('Para Δ = b² - 4.a.c'
      '\n Δ = ', delta)

rd1=delta**1/2

r1=(-b + rd1 ) / (2 * a)
r2=(-b - rd1 ) / (2 * a)
print('Para -b + √Δ)/2a a raíz é: ', r1,
      '\n Para -b - √Δ)/2a a raíz é: ', r2)

# import math
# num = float(input("Entre com um número:\n"))
# raiz = math.sqrt(num)
# print(f'\nA raiz quadrada de {num} é {raiz}\n')

#Converter a temperatura em Celsius e Fahrenheit
# tipo=(int(input('Informe 1 para Celsius ou 2 para Fahrenheit: ')))
# while tipo<1 or tipo>2:
#       tipo=(int(input('Valor incorreto, informe 1 para Celsius ou 2 para Fahrenheit: ')))
# if tipo==1:
#       valorC=int(input('Informe a temperatura para conversão: '))
#       calcC=((valorC*9)/5)+32
#       print('O valor de {} °C equivale a {} °F'.format(valorC, calcC))
# else:
#       valorF=int(input('Informe a temperatura para conversão: '))
#       calcF=((valorF-32)*5)/9
#       print('O valor de {} °F equivale a {} °C'.format(valorF, calcF))


#Informar se o numero é positivo ou negativo
# a=int(input('Digite um valor: '))
# if a<0:
#       print('O valor informado é negativo.')
# else:
#       print('O valor informado é positivo.')


# Informar quantos numeros primos há em um intervalo
# a=int(input('Informe o número a ser verificado: '))
# for num in range (a+1):
#       div = 0
#       qtd = 0
#       for x in range (1, num+1):
#             #qtd=0
#             resto = num % x #print(x, resto)
#             if resto==0:
#                   qtd=div=div+1
#                   #qtd = div + 1
#
#       if div==2:
#             print(num)
#             #print('Existe {} números primos neste intervalo.'.format(qtd))
#       if qtd >= 1:
#             print('Existe {} números primos neste intervalo.'.format(qtd))


#Mostrar os numeros primos de uma sequencia
# num=int(input('Informe o número a ser verificado: '))
# for num in range (1, num+1):
#       div=0
#       for x in range (1, num+1):
#             resto = num % x #print(x, resto)
#             if resto==0:
#                   div=div+1
#       if div==2:
#             print(num)


#Informar se o número é par ou impar
# a=int(input('Informe o número a ser verificado: '))
# div=0
# for x in range (1, a+1):
#       resto = a % x
#       if resto==0:
#             div=div+1
# if div==2:
#       print('O número {} é primo.'.format(a))
# else:
#       print('O número {} não é primo.'.format(a))


# Calculo de juros simples
# c=int(input('Insira o valor do Capital: '))
# i=int(input('Insira a taxa mensal de empréstimo: '))
# n=int(input('Insira o período em meses para pagamento: '))
# j=(c*(i/100)*n)
# m=j+c
# print('O total de juros a ser pago será de R$ {}'.format(j), ' e o montante final de R$ {}'.format(m))

#Qual o valor de venda de um carro
#
# custo=int(input('Insira o valor de Fábrica: '))
# imposto=int(input('Insira o percentual de impostos: '))
# lucro=int(input('Insira o percentual de lucro: '))
# vendedor=int(input('Insira o percentual de comissão do vendedor: '))
#
# if vendedor==0:
#       venda = custo + (custo * (imposto / 100)) + (custo * (lucro / 100))
# else:
#       venda=custo+(custo*(imposto/100))+(custo*(lucro/100))+(custo*(vendedor/100))
#
# print('O valor de venda do veículo será de: {}'.format(venda))

#Tabuada de SOMA:
# soma=int(input('Informe o numero da tabuada a ser somado:'))
#
# for x in range (11):
#       #while x<=10:
#             print(x, ' + ', soma, ' = ', x+soma)
#             x=soma

#Tabuada de MULTIPLICAÇÃO:
# multi=int(input('Informe o numero da tabuada a ser multiplicado:'))
#
# for x in range (11):
#       #while x<=10:
#             print(x, ' x ', multi, ' = ', x*multi)
#             x=multi