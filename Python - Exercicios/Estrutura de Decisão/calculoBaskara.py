#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário
# nas seguintes situações:
#- Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve
#  fazer pedir os demais valores, sendo encerrado;
#- Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#- Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#- Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

print('Vamos calcular as raízes na fórmula de Báskara para funções do tipo ax² + bx + c \n')
#import math
a=(float(input('Informe o valor de a: ')))
if a ==0:
    print('\nSe o valor de a = 0, então a função não é de segundo grau!')
    print('\n*** FIM DO PROGRAMA! ***\n')
else:
    b=(float(input('Informe o valor de b: ')))
    c=(float(input('Informe o valor de c: ')))
    delta=((b*b)-4*a*c)

    if delta < 0:
        print('\nO valor de delta foi: {}'. format(delta))
        print('\nPara os valores informados delta teve valor negativo e não possui raízes reais!')
        print('\n*** FIM DO PROGRAMA! ***\n')
    elif delta == 0:
        print('\nO valor de delta foi: {}'. format(delta))
        print('\nPara os valores informados delta teve valor de 0 e possui apenas 1 raíz real')
        
        print('\nPara Δ = b² - 4.a.c'
              '\n Δ = ', delta)

        rd1=delta**(0.5)

        r1=(-(b) + (rd1) ) / (2 * a)
        r2=(-(b) - (rd1) ) / (2 * a)
        print(' Para -b + √Δ)/2a a raíz é: ', r1,
          '\n Para -b - √Δ)/2a a raíz é: ', r2)
    else:
        print('\nO valor de delta foi: {}'. format(delta))
        print('\nPara os valores informados delta teve 2 raízes reais')
        
        print('\nPara Δ = b² - 4.a.c'
              '\n Δ = ', delta)

        rd1=delta**(1/2)

        r1=(-b + rd1 ) / (2 * a)
        r2=(-b - rd1 ) / (2 * a)
        print(' Para -b + √Δ)/2a a raíz é: ', r1,
          '\n Para -b - √Δ)/2a a raíz é: ', r2)