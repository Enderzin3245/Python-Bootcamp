#metodo construtor

#sempre executado quando umaa nova instancia da classe e criada
#sempre executado primeiro
#__init__

class Cachorro:
    def __init__(self, nome , cor ,acordado=True):
        print()

#metodo destrutor

#sempre executado quando uma instancia é destruida
#pouco usado por causa do coletor de lixo Python
#sempre executado por ultimo

class Cachorro:
    def __del__(self):
        print("Foi destruido")