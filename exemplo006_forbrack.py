pessoas_presentes = ['jonh Snow','jesse pinkman','aria stark','tayrion lannister']
#quero saber se uma pessoa especifica esta presente
chamada = 'aria stark'
for pessoa in pessoas_presentes:
    if pessoa == chamada:
        print('{} esta presente.'.format(chamada))
        break
    else:
        print('só um print para mostrar que for passou por essa pessoa:' + str(pessoa))   



pessoas_presentes = ['jonh Snow','jesse pinkman','aria stark','tayrion lannister']
#quero saber se uma pessoa especifica esta presente
chamada = 'aria stark'
for pessoa in pessoas_presentes:
    if pessoa == chamada:
        print('{} esta presente.'.format(chamada))
        break
    else:
        print('só um print para mostrar que for passou por essa pessoa:' + str(pessoa))   
        continue