#polimorfismo
#o mesmo nome de função (mas assinaturas diferentes)
#sendo usado para tipos diferentes

#capacidade de ser comportar de diversas maneiras
#dependendo da variavel

#EX:
len("python")
len[10 , 20 ,30]

#polimorfismo na herança

#é possivel modificar um metodo em uma classe filha
#herdada da classe pai

class passaro:
    def voar(self): pass #criando o def voar

class pardal(passaro):
    def voar(self): pass #modifcando o voar
    print("pardal voa")

class galinha(passaro):
    def voar(self): pass #modifcando o voar
    print("galinha não voa")


def plano_de_voo(obj): #função que recebe a class pai
    obj.voar()

plano_de_voo(pardal()) #mostar o def do pardal
plano_de_voo(galinha()) #mostra o def da galinha