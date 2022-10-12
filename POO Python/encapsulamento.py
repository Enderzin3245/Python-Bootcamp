#encapsulamento
#modo de agrupar e proteger dados e os metodos que manipulam
#esses dados em uma unidade

#recursos publicos e privados

#usamos convenções no nome do recurso para definir se a
#variavel e publica ou privada
#Não existem palvras reservadas

#u uso do privado e publico so serve para interpretação
#pois nao impedir o seu funcionamento e funções

class veiculo:
    def __init__(self, nome , cor , data):
        self.nome = nome #publicos 
        self.cor = cor #publicos
        self.data = data #publicos
    
    def ligar_motor(self): #publicos
        print("ligando motor")

    def informar_data(self ,valor):
      self.data = valor

c = veiculo("moto" , "preto" , "")
c.informar_data("2014")

#property()
#criar atributos gerenciados em suas classes
#quando precisar modificar sua implementação interna

class foo:
    def __init__(self,x=None):
        self._x = x

    @property #indicar o atributo como metodo
    def x(self):
        return self._x or 0

    @x.setter  #atribuir ou altera valor
    def x(self, value):
        self._x += value 

    @x.deleter #deletar a variavel
    def x(self):
        self._x = - 1


foo = foo(10)
print(foo.x)
foo = 10
print(foo.x)

# / / / / /

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def idade(self):
        _ano_atual = 2022
        return _ano_atual - self._ano_nascimento


pessoa = Pessoa("Guilherme", 1994)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")

    


