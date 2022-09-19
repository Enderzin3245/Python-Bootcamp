#indentação / / / / /
#A identação no python funciona com base no espaçamento

from codecs import oem_decode
from operator import truediv


def sacar(self, valor: float): #inico do bloco metodo

    if self.saldo >= valor: #inicio do bloco if

        self.saldo -= valor

    #fechamento do bloco if

sacar()#fechamento do bloco metodo

#estruturas condicionais / / / / / 
#criam e realizam condições no codigo

idade = 19

if(idade >=18):
    print("ele e maior de idade")

else:
    print("ele não e maior de idade")

    #para a continução do codigo,a condição if precisa ser verdadeira
    #o else será executado quando a condição if for falsa

opção = int(input(1 , 2 ))

if(opção == 1):
    print("primeira opçao")

elif(opção == 2):
    print("segunda opçao")

else:
    print("opçao obrigatoria caso as outras sejam false")

#elif tem o mesmo significado do (if else)

#if aninhado / / / / /
#ifs,elif,else dentro de ifs,elifs,elses

conta_normal = True
saque = 500
saldo = 1000
cheque_especial = 300
conta_universitaria = False

if conta_normal:

    if saldo >= saque:
        print("saque realizado")
    elif saque <= (saldo + cheque_especial):
        print("saque realizado com sucesso")

elif conta_universitaria:

    if saldo >= saque:
        print("saque realizado")
    else:
        print("erro no saque")

#if ternário
#condição escrita em uma linha
#verificação simples

status = "Sucesso" if saldo >= saque else "Falha"
#true status = "Sucesso"
#False status = "Falha"

#estruturas de repetição / / / / /

#for / / / /

texto = input("informe um texto:")
vogais = "AEIOU"

for letra in texto:
    if letra.upper() in vogais:
        print(letra, end="")

else:
    print() #adiciona uma quebra de linha
    #executa  no final do codigo

#informando o nome "Python"
#letra == p em seguida y em seguida t e assim por diante
#esse codigo irá separar a quantidade de vogais e digita-las

#função range e usada ora oriduzir uma sequencia de numeros a partir de um inicio
list(range(4))
#resultado = 0, 1 ,2 ,3


#usando os dois

for numero in range(11):
    print(numero, end="")
#resultado 0,1,2,3,4,5,6,7,8,9,10

#range possui 3 atributos inicio,fim e step
for numero in range(0 , 51 ,5):
    print(numero, end="")
#resultado 0,5,10,15,20,25 ate 50

#while / / / /

opcao = -1

while opcao != 0:
    opcao = int(input("1 Sacar" , "2 extrato" "0 Sair \n"))

    if opcao == 1:
        print("sacar")

    if opcao == 2:
        print("extrato")

#enquanto a var opcao for diferente de 0 executará pra sempre
#o break também serve para enserrar o codigo
#continue serve pra pular uma condiçao ex: opcao == 12 continue (nao informará o 12)


