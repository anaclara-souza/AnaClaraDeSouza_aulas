produtos = ['tv','celular','mouse','teclado','tablete']
item_usuario = input('qual item deseja remover?')
try:
    produtos.remove(item_usuario)
    print(produtos)
except:
    print('O produto {} nao existe na lista.'.format(item_usuario))