lista= [3,5,9,4,1,7]
lista_texto=['gato', 'zebra', 'pato', 'rato', 'arara',]

lista.sort() #ordena em ordem crescente
lista_texto.sort() #ordena em ordem alfabética
print(lista)
print(lista_texto)

lista_texto.reverse() #ordena decresente alfabetica
print(lista_texto)

# print(lista_texto[1]) #irá imprimir o texto da 2 posição, pois conta do 0
# print(sum(lista)) #imprime o somatório dos valores da lista
# print(max(lista)) #immprime o maior valor da lista, para o menor usa min
#
# if 'lobo' in lista_texto: #verifica se há o texto na lista
#     print('Existe lobo na lista')
# else:
#     print('Não existe lobo na lista. Será incluído')
#     lista_texto.append('lobo')
#     print(lista_texto)
#lista_texto.pop(1) #pop retira da lista a posição em parenteses, sem informar retira o ultimo da lista.
#print(lista_texto)
# lista_texto.remove('rato') #remove da lista a string informada.
# print(lista_texto)
