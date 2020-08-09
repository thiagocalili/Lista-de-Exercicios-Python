class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True
    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1
    def diminiu_canal (self):
        if self.ligada:
            self.canal -= 1


televisao = Televisao()
print(televisao.ligada)
televisao.power()
print(televisao.ligada)
televisao.power()
print(televisao.ligada)
print ('Canal: {}'.format(televisao.canal))
televisao.power()
print(televisao.ligada)
televisao.aumenta_canal()
televisao.aumenta_canal()
print('Canal: {}'.format(televisao.canal))
televisao.diminiu_canal()
print('Canal: {}'.format(televisao.canal))




# class Calculadora:
#     def soma(self, valor_a, valor_b):
#         return valor_a + valor_b
#     def subtracao (self, valor_a, valor_b):
#         return valor_a - valor_b
#     def multiplicacao (self, valor_a, valor_b):
#         return valor_a * valor_b
#     def divisao (self, valor_a, valor_b):
#         return valor_a / valor_b
#
# calculadora = Calculadora ()
# print(calculadora.soma(10,2))
# print(calculadora.subtracao(50,20))
# print(calculadora.multiplicacao(20,4))
# print(calculadora.divisao(20,10))


# class Calculadora:
#     valor_a = int(input('Informe o valor do primeiro número: '))
#     valor_b = int(input('Informe o valor do segundo número: '))
#     def __init__(self, num1, num2):
#         self.valor_a= num1
#         self.valor_b= num2
#     def soma(self):
#         return self.valor_a + self.valor_b
#     def subtracao (self):
#         return self.valor_a - self.valor_b
#     def multiplicacao (self):
#         return self.valor_a * self.valor_b
#     def divisao (self):
#         return self.valor_a / self.valor_b
# calculadora = Calculadora (10,2)
# print(calculadora.soma())
# print(calculadora.subtracao())
# print(calculadora.multiplicacao())
# print(calculadora.divisao())

# print(soma(a,b))
# print(subtração (a,b))
# print(multiplicacao(a,b))
# print(divisao(a,b))


# Característica das listas [] , da Tupla (), conjunto {}
# conjunto={1,2,3,4}
# conjunto.add(5)
# conjunto.discard(2)
# print(conjunto)
#
# conjunto={1,2,3,4,5}
# conjunto2={5,6,7,8,9}
# conjunto-uniao=conjunto.union(conjunto2)
# print(conjunto-union) #resultado será {1,2,3,4,5,6,7,8,9} - ira iliminar a duplicitade do 5
#
# conjunto_interseccao=conjunto.intersection(conjunto2) #irá imprimir {5}
# conjunto_diferenca=conjunto.difference(conjunto2) #ira imprimir {1,2,3,4} sao os numeros que nao tem no conjunto1
# conj_diff_simetrica=conjunto.symmetric_difference(conjunto2)
# print('Diferença simétrica:{}'.format(conj_diff_simetrica)) #imprime numeros diferentes entre os conjuntos
#
# conjunto_a={1,2,3}
# conjunto_b={1,2,3,4,5}
#
# conjunto_subset=conjunto_a.issubset(conjunto_b)
# print(conjunto_subset) #informa se um conjunto é sub de outro (todo o a está em b)
#
# conjunto_superset=conjunto_b.issuperset(conjunto_a)
# print(conjunto_subset) #informa se um conjunto é superior ao outro (b maior que a)

