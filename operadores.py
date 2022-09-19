#operadores aritmeticos / / / / / /
#python segue as ordens matematicas

#operadores simples: + - * / // 

#modulo

print(10 % 3)
#resultado:1 resto da divição

#exponenciação

print(2 ** 3)
# resultado:8 

#operadores de comparação

saldo = 450
saque = 200

print(saldo == saque)
#retornará um valor booleano (false)
#== igual

print(saldo != saque)
#retornará um valor booleano (true)
#!= diferente

#além dos mais comuns > < >= <=

#operadores de atribuição

#atribuição simples =
igual = 10

#adição

igual = 10
igual += 2

#irá adicionar 2 a 10
#resultado = 12
#resulta o mesmo para subtração,multiplicação e divisão
#funcinará também com o modulo(resto da divisão) e exponenciação

#operadores lógicos
saldo = 1000
saque = 200
limite = 100

saldo <= saque
#retorna false

saldo >= saque and saque <= limite
#e necessario que ambos sejam verdadeiros para retorná true
saldo >= saque or saque <= limite
#necessario apenas 1 verdadeiro para que retorne true

not 1000 > 1500
not "saque 1500;"
not ""
#reverte o valor obtido true = false false = true
#uso dos parênteses para melhor organização

#operadores de identidade
#compara variaveis que estao na mesma posição

curso = "curso"
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso
#retorna true pois utilizam a mesma região da memoria

curso is not nome_curso
#reverte o valor obtido true = false false = true

#operadores de associação
#verificam se um objeto esta presente em uma sequência
curso = "Curso de python"
frutas = ["laranja","uva", "limão"]
saques = [100 , 500]

"python" in curso
#retorna true pois a palavra está presente

"maça" not in frutas
#retornará true pois reverte o valor dado

200 in saques
#retorna false

