#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

ano = int(input('Informe o ano: '))
mes = int(input('Informe o mês: '))
dia = int(input('Informe o dia: '))
lista31 = [1, 3, 5, 7, 8, 10, 12]
lista30 = [4, 6, 9, 11]

if mes in lista31:
    if dia > 0 and dia < 31:
        print('A data {}/{}/{}, é uma data válida!'.format(dia, mes, ano))
    else:
        print('A data {}/{}/{}, NÃO é uma data válida!'.format(dia, mes, ano))
elif mes in lista30:
    if dia > 0 and dia < 30:
        print('A data {}/{}/{}, é uma data válida!'.format(dia, mes, ano))
    else:
        print('A data {}/{}/{}, NÃO é uma data válida!'.format(dia, mes, ano))
elif mes == 2 or (ano%4 == 0 and ano%100 !=0) or ano%400 == 0:
    if dia > 0 and dia < 29:
        print('A data {}/{}/{}, é uma data válida!'.format(dia, mes, ano))
    else:
        print('A data {}/{}/{}, NÃO é uma data válida!'.format(dia, mes, ano))
else:
    print('A data {}/{}/{}, NÃO é uma data válida!'.format(dia, mes, ano))

