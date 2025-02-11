#Faça um programa que receba uma nota do aluno e se for SUPERIOR ou IGUAl a 7 apareça 
# a mensagem que ele esta APROVADO se for INFERIOR a 5ele esta "Nao aprovado/reprovado direto" e se estiver entre 
#e e 7 apareça a mensagem "nao aprovado recuperaçao"
num = int(input("Digite sua nota: "))
if num > 7:
   print("APROVADO")
else:
    if num < 5 :
        print("VOCE ESTA REPROVADO!!")
    else:
        print("RECUPERAÇAO/NAO APROVADO")
