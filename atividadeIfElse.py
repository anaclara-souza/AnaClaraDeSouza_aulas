#faça um programa que o usuario digite um numero e diga se o numero e superior a 20 inferior a 10 ou se esta entre 10 e 20
num = int(input("Digite um numero: "))
if num > 20:
   print("O numero è maior que 20")
else:
    if num < 10 :
        print("O numero é inferior a 10")
    else:
        print("O numero esta entre 10 e 20")