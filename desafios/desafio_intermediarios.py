letra = input() 

alfabeto = list("0ABCDEFGHIJKLMNOPQRSTUVWXYZ")

if letra in alfabeto:
    print(alfabeto.index(letra))


#desafio 2

txt = input()
opcao = txt.split()
verdade = 0

while verdade == 0: 

      
        if opcao[0] == "esquerda":
            print("ingles")
          
              
        if opcao[1] == "direita":
            print("frances")
            

        if opcao[2] == "nenhuma":
            print("portugues")
           

        if opcao[3] == "ambas":
            print("caiu")
            break
       
  
