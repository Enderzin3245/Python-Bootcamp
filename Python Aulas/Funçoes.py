#Funções / / / /

#bloco de código que possui um nome e pode apresentar parâmetros

from os import O_RDONLY


def exibir_mensagem():
    print("ola mundo")

#Com parâmetros

def exibir_mensagem_2(nome):
    print(f"seja bem vindo {nome}")

def exibir_mensagem_3(nome = "Antonio"):
    print(f"seja bem vindo {nome}")

#chamando a variavel
exibir_mensagem()
exibir_mensagem_2(nome = "antonio")
exibir_mensagem_3()

#toda função tem como return(none)
#mais podemos mudar adicionando return

def calcular_total(numeros):
    return sum(numeros)

calcular_total([10 , 20 ,30]) #60

def retorna_numero(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor,sucessor

retorna_numero(10) #9 , 11

#argumentos nomeados
#aqueles que passamos chave e valor

def salvar_carro(marca,modelo,ano,placa):
    print(f"marca: {marca} modelo: {modelo} ano: {ano} placa: {placa}")

salvar_carro("tesla" , "fiat" , "2014" , "23096")#passando normal
salvar_carro(marca = "fiat" , modelo = "uno", ano = "2012" ,placa = "297645")#passando com as chaves

#Args e Kwargs
#tupla e dicionario respectivamente

salvar_carro(**{"marca": "fiat" , "modelo": "uno", "ano": "2012" ,"placa": "297645"})
#Passando um dicionario como parâmetro


#parâmetros especiais


#positional only
def salvar_carro2(marca,modelo,ano, /, placa , tipo , moto):
    print()

salvar_carro2("palio", "uno" , "2014", placa="2020", tipo="hshvgw" , moto="titan")
#antes da barra os nomes são passados obrigatoriamente por posição,depois dela há a nomeção ou posição

#keyword only
def salvar_carro3(*,marca,modelo,ano, placa , tipo , moto):
    print()

salvar_carro3(marca = "palio" , modelo = "uno", ano = "2020",placa="2020", tipo="hshvgw" , moto="titan")
#uso do asterisco faz de obrigatorio a nomeação

#combinados

def salvar_carro4(marca,modelo,ano, /, *,placa , tipo , moto):
    print()

salvar_carro4("palio", "uno" , "2014",placa="2020", tipo="hshvgw" , moto="titan")
#uso combinado obriga o uso da posição e nomeação respectivamente

#Objetos de primeira classe
#objetos que podem ser usados em funções,receber variaveis e serem usados em Return


#Extendendo funções
def somar(a,b):
    return a + b

def exibir(a, b, funcao):
    resultado = funcao(a,b)
    print(f"O resultado da operação{a} + {b} = {resultado}")

exibir(10,10 , somar) #o resultado da operação é 10 + 10 = 20

#escopo global, podemos informar em um escopo local uma variavel global usando a palavra global

salario = 2000

def salario(bonus):
    global salario #escopo global no local
    salario =+ bonus
    return salario

salario(500)






