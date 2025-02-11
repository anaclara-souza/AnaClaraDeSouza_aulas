#trasforma apenas a primeira letra de uma string em maiuscula
nome = "ana"
print(nome.capitalize(),"\n")

#trasforma apenas a primeira letra de uma string em minuscula
nome = "ANA"
print(nome.casefold(),"\n")


#Conta o numero de vezes que um caractere especifico aparece na string
nome = "AnaClaraSouza@gmail.com"
print(nome.count('a'),"\n")


#RETORNA true (verdadeiro) OU false (falso) para um teste se a string termina com uma string especifica.
nome = "AnaClaraSouza@gmail.com"
print(nome.endswith('gmail.com'),"\n")


#Encontra a posiçao do termo procurado.lembre-se começa do do zero
nome = "AnaClaraSouza@gmail.com"
print(nome.find('@'),"\n")


#verifica se o texto é todo feito com letras.
nome = "Ana@"
print(nome.isalpha(),"\n")


#Verifica se o texto e feito com numeros.
nome = "677"
print(nome.isnumeric(),"\n")


#Substitui um caractere escolhido por outro.
nome = "ana"
print(nome.replace('a','u'),"\n")


#separa o texto string baseado em algum caractere indicado.
nome = "Ana Clara Souza @ gmail .com"
print(nome.split('@'),"\n")

#colocar todas as letras iniciais em maiuscula.
nome = "ana clara de souza"
print(nome.title(),"\n")


#Retira os caracteres indesejados,como por exemplos espaços que nao agregam valor.
nome = "  Ana Clara Souza  "
print(nome.strip(),"\n")


#Retorne true ou false para um teste de uma string se inicia com um texto especifico.
nome = "Ana 2008"
print(nome.startswith("ana "),"\n")
print(nome.startswith("ana"),"\n")