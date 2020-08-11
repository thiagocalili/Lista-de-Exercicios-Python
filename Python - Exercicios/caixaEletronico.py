# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque
# e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão
# as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100,
# uma nota de 50, uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100,
# uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
"""
def check_dezena(intDezena):
    if intDezena == 5:        
        print(' 1 nota de R$ 50')
    elif intDezena > 5:
        dezenas = intDezena - 5
        print(' 1 nota de R$ 50')
        print(' {} nota(s) de R$ 10'.format(dezenas))
    elif intDezena > 0 and intDezena < 5:
        print(' {} nota(s) de R$ 10'.format(intDezena))
        
def check_unidade(intUnidade):
    if intUnidade == 5:       
        print(' 1 nota de R$ 5')
    elif intUnidade > 5:
        unidades = intUnidade -5
        print(' 1 nota de R$ 5')
        print(' {} nota(s) de R$ 1'.format(unidades))
    elif intUnidade > 0 and intUnidade < 5:
        print(' {} nota(s) de R$ 1'.format(intUnidade))
    else:
        pass


print(' ')
print('-------------------------------------------------------------------------------------')
print('                           BEM VINDO AO CAIXA ELETRÔNICO                             ')
print('-------------------------------------------------------------------------------------')
print('  Informamos que o valor mínimo para saque é de R$ 10 reais e o máximo R$ 600 reais  ')
print('-------------------------------------------------------------------------------------')
valorSaque = int(input('  Informe o valor de saque R$ '))
print('-------------------------------------------------------------------------------------')
saqueStr = str(valorSaque)

if len(saqueStr) == 1:
    unidade = int(saqueStr)
    check_unidade(unidade)

elif len(saqueStr) == 2:
    unidade = int(saqueStr[-1])
    dezena = int(saqueStr[0])
    
    check_dezena(dezena)
    check_unidade(unidade)

elif len(saqueStr) == 3:
    unidade = int(saqueStr[-1])
    dezena = int(saqueStr[-2])
    centena = int(saqueStr[0])
    
    print(' O saque terá as seguintes notas: ')
    print(' {} nota(s) de R$ 100!'.format(centena))
    check_dezena(dezena)
    check_unidade(unidade)
else:
    print('Indisponível')

print(' ')
"""
########################################################################################
# CAIXA SEGUNDA FORMA DE CÓDIGO:
"""
while True: # enquanto não digitar um valor válido, pede que digite novamente
    try:
        valor = int(input('Digite o valor (entre 10 e 600):'))
        if 10 <= valor <= 600:
            break # valor válido, sai do while
        # se não entrou no if acima, o valor é inválido
        print('valor deve estar entre 10 e 600')
    except ValueError: # não foi digitado um número
        print('Digite um número válido')

# todas as notas possíveis
notas = [100, 50, 10, 5, 1]

for nota in notas:
    if valor >= nota:
        qtd = valor // nota # divisão exata (sem considerar casas decimais)
        print(f'{qtd} notas de {nota}')
        valor %= nota # resto da divisão
"""

########################################################################################
# CAIXA TERCEIRA FORMA DE CÓDIGO:
"""
print(' ')
print('-------------------------------------------------------------------------------------')
print('                           BEM VINDO AO CAIXA ELETRONICO                             ')
print('-------------------------------------------------------------------------------------')
print('  Informamos que o valor mínimo para saque é de R$ 10 reais e o máximo R$ 600 reais  ')
print('-------------------------------------------------------------------------------------')
valorSaque = int(input('  Informe o valor de saque R$ '))
print('-------------------------------------------------------------------------------------')

if valorSaque < 10 or valorSaque > 600:
  print('Valor inválido')
else:
  qtdeNotasCem = valorSaque // 100
  qtdeNotasCinquenta = (valorSaque % 100) // 50
  qtdeNotasVinte = (valorSaque % 50) // 20
  qtdeNotasDez = ((valorSaque % 50) // 10) - (2 * qtdeNotasVinte)
  qtdeNotasCinco = (valorSaque % 10) // 5
  qtdeNotasDois = (valorSaque % 5) // 2
  qtdeMoedasUm = (valorSaque % 5) - (2 * qtdeNotasDois);

  print('O saque terá as seguintes notas: ')
  print('    {0:d} nota{1} de R$ 100!'.format(qtdeNotasCem, 's' if qtdeNotasCem > 1 else ''))
  print('    {0:d} nota{1} de R$ 50!'.format(qtdeNotasCinquenta, 's' if qtdeNotasCinquenta > 1 else ''))
  print('    {0:d} nota{1} de R$ 20!'.format(qtdeNotasVinte, 's' if qtdeNotasVinte > 1 else ''))
  print('    {0:d} nota{1} de R$ 10!'.format(qtdeNotasDez, 's' if qtdeNotasDez > 1 else ''))
  print('    {0:d} nota{1} de R$ 5!'.format(qtdeNotasCinco, 's' if qtdeNotasCinco > 1 else ''))
  print('    {0:d} nota{1} de R$ 2!'.format(qtdeNotasDois, 's' if qtdeNotasDois > 1 else ''))
  print('    {0:d} moeda{1} de R$ 1!'.format(qtdeMoedasUm, 's' if qtdeMoedasUm > 1 else ''))

"""