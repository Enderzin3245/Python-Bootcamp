#metodos da classe string
curso = "python"

curso.upper() #uppercase
curso.lower() #lowercase
curso.title() #titlecase

curso.strip() #sem espaços brancos
curso.lstrip() #sem espaços na esquerda
curso.rstrip() #sem espaços na direita

#listas
#há varias tipos de listas
lista = ["11" , "gustavo" , "tiago"]
lista = list(range(10))

#podemos realizar varias coisas

lista.append(1) #adicionar algo a lista
lista[0] #pegar item na posição
lista.remove("11") #remove algo da lista
lista.count("11") #conta a quantidade desse elemento
max(lista) #mostra o maior valor
min(lista) #mostra o menor valor
lista.extend("gato") #adiciona a lista
lista.sort() #organiza a lista do menor ao maior numero

#tuplas
#listas que são imutaveis
tuplas = ("gustavo" , 12 , "valber")
#não há como remover valores na tupla ou trocar

#dicionarios
#dicionarios recebem uma chave e valor

dc = {"numero":20 , "gustavo":10 , "12":5 }
dc["gustavo"] #retona a chave 10
dc["gustavo"] = 25 #trocando o valor da chave
dc.keys() #retornando todos os valores da chava
dc.setdefault("limao" , 23) #vendo caso ja exista essa chave,ser nao existe ela o adiciona


print(curso.center(10 , "#"))
#texto centralizado em 10 letras ##python##
print(".".join(curso))
# "p.y.t.h.o.n"


#interpolação de variáveis

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
lista = ["p" , "y" , "t" , "h" , "o" , "n"]

nome[0] lista[0]
#"G" letra na posição
nome[:9] lista[:4]
#Gustavo m ate a posição informada
nome[10:]
#"reira de lima" a partir da posição informada
nome[8:15]
#"moreira" entre as posições
nome[2:4:6] 
#"utv" letras selecionadas
nome[:] lista[::]
#espelha a variavel
nome[: -1] lista[::-1]
#espelha ao contrario


#esse tipo de fatiamento pode ser realizado com listas também

#strings triplas / / / / /

mensagem = f""" ola meu nome 
    é gustavo,  
        tenho 17 anos"""
#ele mantem o espaçamento digitado
