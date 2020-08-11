# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser
# um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;
print(' ')
print('Para verificar o tipo do triângulo, informe a seguir os lados.')
print(' ')
lado1 = float(input('Informe o valor do primeiro lado: '))
lado2 = float(input('Informe o valor do segundo lado: '))
lado3 = float(input('Informe o valor do terceiro lado: '))

print(' ')

if lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
    print('''O triângulo é EQUILÁTERO, pois possuem 3 lados iguais:
            \n''','Lado 1: ', lado1,'\n Lado 2: ', lado2,'\n Lado 3: ', lado3)

elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print('''O triângulo é ESCALENO, pois todos os lados são diferentes:
            \n''','Lado 1: ', lado1,'\n Lado 2: ', lado2,'\n Lado 3: ', lado3)
else:
    print('''O triângulo é ISÓSCELES, pois possuem 2 lados iguais:
            \n''','Lado 1: ', lado1,'\n Lado 2: ', lado2,'\n Lado 3: ', lado3)

print(' ')