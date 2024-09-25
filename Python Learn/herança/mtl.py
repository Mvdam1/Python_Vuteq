class Animal:
    def __init__(self,nro_patas,Cor):
        self.nro_patas = nro_patas 
        self.Cor = Cor
      
class Mamifero(Animal):
     def __init__(self,nro_patas,Cor,**kw):
        self.nro_patas = nro_patas 
        self.Cor=Cor
        super().__init__(**kw)
class Ave(Animal):
         def __init__(self,nro_patas,Cor_Bico):
            self.nro_patas = nro_patas 
            
           
class Cachorro(Mamifero):
    pass
class Gato(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    pass

gato = Gato(4,"Preto")
Perry =Ornitorrinco(4,"Verde","Laranja")
print(gato.Cor)
print(Perry.Cor)