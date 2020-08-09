
a=int(input('Insira a primeira nota: '))
while a>25:
    a=int(input('Nota inválida. Digite a nota correta: '))
b=int(input('Insira a segunda nota: '))
while b>25:
    b=int(input('Nota inválida. Digite a nota correta: '))
c=int(input('Insira a terceira nota: '))
while c>25:
    c=int(input('Nota inválida. Digite a nota correta: '))
d=int(input('Insira a quarta nota: '))
while d>25:
    d=int(input('Nota inválida. Digite a nota correta: '))
media=int(a+b+c+d)/4
print('A média das notas é: {}'.format(media))


# nota=int(input('Digite o valor da nota:'))
# while nota>25:
#     nota=int(input('Valor incorreto. Digite o valor da nota: '))


# a=0
# while a<=10:
#     print (a)
#     a=+1


#Para imprimir os numeros primos de um intervalo:
# a=int(input('Entre com um valor: '))
# for num in range (a):
#     div=0
#     for x in range (1, num+1):
#         resto= num % x
#         if resto==0:
#             div+=1
#     if div==2:
#         print(num) #neste caso irá imprimir todos os numeros primos.


#Usuario digita um numero e informar se o numero é primo ou não:
# a=int(input('Digite um número: '))
# div=0
# for x in range (1, a+1):
#     resto= a % x
#     if resto==0:
#         div=div+1 #pode ser usado div+=1, concatenando que o div irá sempre receber ele mesmo mais 1.
# if div==2:
#     print('O número {} é primo.'.format(a))
# else:
#     print('O número {} não é primo'.format(a))

# for x in range (1, 100): # PARA x EM sequencia de 1 até 100 e imprima os números
#     print (x)

#Para saber se um número é par ou ímpar
# a=int(input('Entre com um valor: '))
# resto=a % 2
#
# if resto ==0: #== significa que o resultado é igual a 0, quando apenas 1 = ele recebe.
#     print('O número é par.')
# else:
#     print('O número é impar.')


#Para saber qual o maior número digitado
# a=int(input('Insira o primeiro valor: '))
# b=int(input('Insira o segundo valor: '))
# c=int(input('Insira o terceiro valor: '))
#
# if a>b and a>c: # os dois pontos indica o fim de IF
#     print('O maior valor é {}'.format(a)) #o tab indica que o print está no bloco do if.
# elif b>a and b>c: #elif significa senao se
#     print('O maior número é {}'.format(b))
# else: #se o valor de 'b' for maior que 'a e c' condição else ira complementar e finalizar o proposição
#     print('O maior número é {}'.format(c))


# a=int(input('Insira o primeiro valor: '))
# b=int(input('Insira o segundo valor: '))
# soma=a+b
# subtracao=a-b
# multiplicacao=a*b
# divisao=a/b
# resto=a%b
#
# print('O valor da soma é: ',soma)
# print('O valor da subtração é: ',subtracao)
# print('O valor da multiplicação é: ', multiplicacao)
# print('O valor da divisão é: ', divisao)
# print('O valor do resto é: ', resto)


# print('soma: {}'.format(soma)) format irá concatenar qualquer tipo de variavel e imprimir.
#Para reduzir linhas pode ser usado da seguinte forma:
#print('Soma: {}. Subtração: {}'.format(soma, subtracao)) - a ordem deve ser a mesma.
# /n (da espaço como o Enter).
#Para que nao haja erros com local das variáveis, pode ser usado o valor dentro das chaves e igualar a variavel:
# print('Soma: {soma}. \n Subtração: {subtracao}'
#         '\n Multiplicação: {multi}'
#         '\n Divisão: {div}'
#         '\n Resto: {resto}'.format(soma=soma,
#                                    subtracao=subtracao,
#                                    multi=multiplicacao,
#                                    div=divisao,
#                                    resto=resto))
# print(type(soma)) - imprime o tipo da váriável str string - int inteiro - float decimal


# meses=int(input('Insira o total de meses: '))
# dias=meses*30
# print('O total em dias dos meses são:', dias)


#Solicitar 4 valores, tirar a media e pedir valores abaixo de 25
# a=int(input('Insira o primeiro valor: '))
# b=int(input('Insira o segundo valor: '))
# c=int(input('Insira o terceiro valor: '))
# d=int(input('Insira o quarto valor: '))
# media=int(a+b+c+d)/4
# if a<=25 and b<=25 and c<=25 and d<=25:
#     print('A média das notas é: {}'.format(media))
# else:
#     print('Alguma nota foi digitada errada.')

# Outro modo para caso erre os valores é solicitar logo após a variavel:

# a=int(input('Insira o primeiro valor: '))
# if a>25:
#     a=int(input('Nota inválida. Digite a nota correta: '))
# b=int(input('Insira o segundo valor: '))
# if b>25:
#     b=int(input('Nota inválida. Digite a nota correta: '))
# c=int(input('Insira o terceiro valor: '))
# if c>25:
#     c=int(input('Nota inválida. Digite a nota correta: '))
# d=int(input('Insira o quarto valor: '))
# if d>25:
#     d=int(input('Nota inválida. Digite a nota correta: '))
# media=int(a+b+c+d)/4
# print('A média das notas é: {}'.format(media))


# num=int(input('Digite um número qualquer: '))
# prox=num+1
# print('O próximo número será: ', prox)


# lado1=int(input('Insira o valor da primeira medida: '))
# lado2=int(input('Insira o valor da segunda medida: '))
# area=lado1*lado2
# print('A área do total será de: ', area,'m²')


# a=int(input('Insira um valor qualquer:'))
# dobro=a*2
# print('O dobro do valor: ',a ,' é ', dobro)


# a=999
# b=555
# print('O valor inicial de A é: ', a)
# print('O valor inicial de B é: ', b)
# temp=a
# a=b
# b=temp
# print ('O valor invertido de A e B são: ', a,b)


# a=int(input('Digite o primeiro valor: '))
# b=int(input('Digite o segundo valor: '))
# soma=a+b
# print('O Resultado da soma é: ', soma)