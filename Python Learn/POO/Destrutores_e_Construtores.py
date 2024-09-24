#Conceitos de desrutrores e construtores 

#metodos init e delet


#__init__.


#from typing import Any

class Cachorro  :
    def __init__(self, nome, cor, idade):
        print("Inicializando classe")
        self.nome = nome
        self.cor = cor
        self.idade = idade
 
    def latir(self):

        print("au au")
    
        
    def __del__(self):
        print("Deletando")    
    
    def dormir (self):
        print("plim")
        print("Estou dormindoq!") 
   
def criar_cachorro():
    zz = Cachorro("Zeus","Marrom",2)
    print(zz.nome)    
         
         
         
    def brincar(self):
        print("O cachorro esta feliz")
 
criar_cachorro()    

# shitzu1 = Cachorro("Lili","Branca",3)
# c = Cachorro("Chappier","Preto",2)
# print(shitzu1.nome)
# c.latir()
# shitzu1.dormir()

