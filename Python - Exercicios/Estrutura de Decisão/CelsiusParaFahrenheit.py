#Converter a temperatura em Celsius e Fahrenheit
 tipo=(int(input('Informe 1 para Celsius ou 2 para Fahrenheit: ')))
 while tipo<1 or tipo>2:
       tipo=(int(input('Valor incorreto, informe 1 para Celsius ou 2 para Fahrenheit: ')))
 if tipo==1:
       valorC=int(input('Informe a temperatura para conversão: '))
       calcC=((valorC*9)/5)+32
       print('O valor de {} °C equivale a {} °F'.format(valorC, calcC))
 else:
       valorF=int(input('Informe a temperatura para conversão: '))
       calcF=((valorF-32)*5)/9
       print('O valor de {} °F equivale a {} °C'.format(valorF, calcF))