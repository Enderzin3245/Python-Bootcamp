#herança / / / / 
#capacidade de uma classe herdar caracteristicas de outra classe

#herança simples
#uma classe filha e uma mãe

from ssl import CertificateError
from unicodedata import name


class A:
    pass

class B(A):
    pass
    #classe B filha da classe A

#herança multipla
#um filho e diversas mãe

class A:
    pass

class B:
    pass
class C(A, B):
    pass
    #classe C filha de B e A

#EX: / / / 

class veiculo:
    def __init__(self, nome , cor , data):
        self.name = name
        self.cor = cor
        self.data = data
    
    def ligar_motor(self):
        print("ligando motor")
    
class moto(veiculo):
    pass

class caminhao(veiculo):
    pass

m = moto("kawsake" , "blue" , "2018")
c = caminhao("wonda" , "preto" , "2016")



class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)


class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)


class Gato(Mamifero):
    pass


class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)


gato = Gato(nro_patas=4, cor_pelo="Preto")
print(gato)

ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo="vermelho", cor_bico="laranja")
print(ornitorrinco)
