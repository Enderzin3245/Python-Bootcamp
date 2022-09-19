#metodos da classe string
curso = "python"

curso.upper() #uppercase
curso.lower() #lowercase
curso.title() #titlecase

curso.strip() #sem espaços brancos
curso.lstrip() #sem espaços na esquerda
curso.rstrip() #sem espaços na direita

print(curso.center(10 , "#"))
#texto centralizado em 10 letras ##python##
print(".".join(curso))
# "p.y.t.h.o.n"

#interpolação de variáveis

#old style %

#.format
nome = "Gustavo"
idade = 17
print("ola me chamo {}. eu tenho {} ." .format(nome , idade))
#.format insere os valores na ordem descrita
print("ola me chamo {2}. eu tenho {1} ." .format(nome , idade))
#ou na ordem chamada
print("ola me chamo {nome}. eu tenho {idade} ." .format(nome = nome , idade = idade))
#ou um identador

#f-string

print( f"ola me chamo {nome}. eu tenho {idade} .")
#apenas passar a propria identação

pi = 3.14159
print(f"Valor de pi {pi:.2f}")
#informará apenas dois valores depois de .
print(f"Valor de pi {pi:10.2f}")
#colocará 10 espaços em branco antes do primeiro número

#Fatiamento / / / /

nome = "Gustavo moreira de lima"

nome[0]
#"G" letra na posição
nome[:9]
#Gustavo m ate a posição informada
nome[10:]
#"reira de lima" a partir da posição informada
nome[8:15]
#"moreira" entre as posições
nome[2:4:6] 
#"utv" letras selecionadas
nome[:]
#espelha a variavel
nome[: -1]
#espelha ao contrario

#strings triplas / / / / /

mensagem = f""" ola meu nome 
    é gustavo,  
        tenho 17 anos"""
#ele mantem o espaçamento digitado
