lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]
lista3 = [11,12,13,14,15]
todas_listas = [lista1,lista2,lista3]
print(todas_listas)

produtos = ['tv','celular','mouse','teclado','tablete']
print(produtos[1])


produtos = ['tv','celular','mouse','teclado','tablete']
vendas = [1000, 1500, 350, 270, 900]
print('As vendas de {} foram de {}'.format(produtos[1],vendas[1]))


produtos = ['tv','celular','mouse','teclado','tablete']
i = produtos.index('mouse')
print('O valor de i é ' + str(produtos[i]))







produtos = ['tv','celular','mouse','teclado','tablete']
estoque = [100,150,100,120,70,180,80]
produto = input('Insira o nome do produto e letra minuscula: ')
if produto in produtos:
    i = produtos.index(produto)
    qtde_estoque = estoque[i]
    print('temos{}unidades de {} no estoque'.format(qtde_estoque,produto))
else:
   print('{}nao existe no estoque'.format(produto))