#metodos abstratos e estaticos
class Teste(object):

  def metodoNormal(self):
   print("Olá sou um método normal")
  

  @classmethod
  def metodoClass(cls, self):
    print("Sou um método de:")
    print(cls)
    print("Chamado por: ")
    print(self)
  @staticmethod
  def metodoStatic():

    print("E sou um método estático")
obj = Teste()
# chamando o método normal
obj.metodoNormal()
# chamando método de classe pela Class e pelo Object
Teste.metodoClass(Teste)
obj.metodoClass(obj)
# chamando método estático
obj.metodoStatic()

#class abstrata

from abc import ABC, abstractmethod, abstractproperty


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
        print("Ligada!")

    def desligar(self):
        print("Desligando a TV...")
        print("Desligada!")

    @property
    def marca(self):
        return "Philco"


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ligado!")

    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Desligado!")

    @property
    def marca(self):
        return "LG"


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)


controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)