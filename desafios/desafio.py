

numero1 = 200
X = 3
Y = 8
soma = X + Y
  
if numero1 > 0 and numero1 < 10000:
  
  if X > 0 and Y < 100:
    
    ICM = numero1 / soma
    
    print(f"{ICM:.2f}")
    
  else:
    print("voce informou um parametro errado")
    
  
else:
  print("voce informou um parametro errado")    


H , P = 10 , 90

if H >= 1 and P <= 1000:
  
  Numero_medio = H / P
  print(f"{Numero_medio:.2f}") 


  Tempo_Gasto = 10
Velocidade_media = 85

Distancia_percorrida = Tempo_Gasto * Velocidade_media
Litros_Gastos = Distancia_percorrida / 12

print(f"{Litros_Gastos:.3f}") 