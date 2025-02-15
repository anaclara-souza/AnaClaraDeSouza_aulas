#consulta do clinte,5 nome,5 telefone,5 bairro

nome = ['ana','claudia','mikey','lana','tabata']
telefone = [47992992109, 4721217212,47892109121,472129221213,47991882112,47821211212,47981278212121]
bairro = ['iririu','comasa','floresta','boa vista','centro']
nomes = input('Insira o nome do cliente e letra minuscula: ')
if nomes in nome:
    i = nomes.index(nome)
    tele = telefone[i]
    print('telefone{}'.format(tele))
    i = nome.index(nomes)
    bai = bairro[i]
    print('bairro:{}'.format(bai))
else:
   print('{}nao tem cadastro'.format(bairro))