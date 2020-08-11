# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas,
# dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades 
# Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

numero = input("Digite um numero menor que 1000: ")
numeroStr = str(numero)
qtNumero = len(numeroStr)

if qtNumero == 3:
    centena = numeroStr[0:1]
    dezena = numeroStr[1:2]
    unidade = numeroStr[2:3]
    
    if (centena == '1' or centena == '0') and (dezena == '1' or dezena == '0') and (unidade == '1' or unidade == '0'):
        print (numeroStr + " = " + centena + " centena , " + dezena + " dezena, " + unidade + " unidade")
    elif (centena != '1' or centena != '0') and (dezena == '1' or dezena == '0') and (unidade == '1' or unidade == '0'):
        print (numeroStr + " = " + centena + " centenas , " + dezena + " dezena, " + unidade + " unidade")
    elif (centena != '1' or centena != '0') and (dezena != '1' or dezena != '0') and (unidade == '1' or unidade == '0'):
        print (numeroStr + " = " + centena + " centenas , " + dezena + " dezenas, " + unidade + " unidade")
    elif (centena != '1' or centena != '0') and (dezena == '1' or dezena == '0') and (unidade != '1' or unidade != '0'):
        print (numeroStr + " = " + centena + " centenas , " + dezena + " dezena, " + unidade + " unidades")
    elif (centena == '1' or centena == '0') and (dezena != '1' or dezena != '0') and (unidade != '1' or unidade != '0'):
        print (numeroStr + " = " + centena + " centena , " + dezena + " dezenas, " + unidade + " unidades")
    elif (centena != '1' or centena != '0') and (dezena != '1' or dezena != '0') and (unidade != '1' or unidade != '0'):
        print (numeroStr + " = " + centena + " centenas , " + dezena + " dezenas, " + unidade + " unidades")    
    elif (centena != '1' or centena != '0') and (dezena == '1' or dezena == '0') and (unidade == '1' or unidade == '0'):
        print (numeroStr + " = " + centena + " centenas , " + dezena + " dezena, " + unidade + " unidade")
    
if qtNumero == 2:
    dezena = numeroStr[0:1]
    unidade = numeroStr[1:2]

    if (dezena == '1' or dezena == '0') and (unidade == '1' or unidade == '0'):
        print (numeroStr + " = " + dezena + " dezena, " + unidade + " unidade")
    elif (dezena != '1' or dezena != '0') and (unidade == '1' or unidade == '0'):
        print (numeroStr + " = " + dezena + " dezenas, " + unidade + " unidade")
    elif (dezena == '1' or dezena == '0') and (unidade != '1' or unidade != '0'):
        print (numeroStr + " = " + dezena + " dezena, " + unidade + " unidades")
    elif (dezena != '1' or dezena != '0') and (unidade != '1' or unidade != '0'):
        print (numeroStr + " = " + dezena + " dezenas, " + unidade + " unidades")

if qtNumero == 1:
    unidade = numeroStr[0:1]
    if (unidade == '1' or unidade == '0'):
        print (numeroStr + " = " + unidade + " unidade")
    elif (unidade != '1' or unidade != '0'):
        print (numeroStr + " = " + unidade + " unidades")