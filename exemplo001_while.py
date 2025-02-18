venda = input('registre um produto: para cancelar o registro de um novo produto, basta apertar enter sem digitar nada. ')
vendas = [];
#crie aqui o programa 
while venda !='':
    vendas.append(venda)
    venda = input('registre um produto: para cancelar o registro de um novo produto, basta apertar enter sem digitar nada.')
    print('Registros Finalizados. As vendas cadastradas foram de:{}'.format(vendas))