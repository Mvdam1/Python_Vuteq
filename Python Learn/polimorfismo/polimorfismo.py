    #O que é polimorfismo?
    #mesmo nome de função mas assinaturas diferentes sendo usados para tipos diferentes
    
    
#ex

# len("Python")
# len([10,20,30])
# print (len)


#polimorfismo com herança 


#exemplo


class Passaro:
    def voar(self):pass
        
class Pardal(Passaro):
    def voar(self):
        print("Voando como um pardal")
        
# FIXME: Exemplo ruim para usar a herança 
class Aviao(Passaro):
    def voar(self):
        print("Voando como um avião")



class Avestruz(Passaro):
    def voar(self):
        print("Voando como uma avestruz, mas avestruz não voa")
    
def plano_de_voo(passaro):
    passaro.voar()  
    
    
def voarr_passaros(obj):
    obj.voar()  #chama a função voar da classe que o objeto obj representa
        
p1 = Pardal()   
p2 = Avestruz()   

plano_de_voo( p2)    
    
# plano_de_voo(Pardal())
# plano_de_voo(Avestruz()) 