#POO propagamação orientada a objetos

#classes
#define caracteristicas e comportamentos de um objeto,porém não e possivel usa-las diretamente
#algo abstrato

#Objetos
#objetos sao todas as formas que podem receber caracteristicas e metodos

#exempls de uma class e a atribuição de seus valores
from distutils import core


class Cachorro:
    def __init__(self, nome , cor ,acordado=True):

        self.nome = nome #Atributos da class
        self.cor = cor
        self.acordado = acordado #atributos

    def latir(self): #metodos da classe
        print("Auau")

    def dormir(self):   #metodos da classe
        self.acordado = False
        print("Zzzzzz")
        retornar = "A" #podemos criar variaveis
        return retornar #podemos retorna-las

    def __str__(self): #podemos usar o metodo str para melhorar representação da class
        return f"Cachorro: {self.cor}, {self.name}" 

    #def __str__(self):
     #   return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor
      #  in self.__dict__.items()])}"


#o uso do self serve para passar ou instanciar o proprio objeto

#objeto instanciando a classe acima
cao_1 = Cachorro("trex" , "marrom" , False)
cao_1.latir()   #chamando o metodo
cao_1.dormir()  #Iguais cao_1.dormir(self)
cao_1.str()

#podemos informar apenas os atributos da classe
print(cao_1.nome , cao_1.cor , cao_1.acordado)

