#Poo são classes ou objetos 
#Conceitos das classes e objetos

#Classes definem as caracteristicas e os comportamentos do objeto, porem nao se pode usala]s diretamente

class Cachorro:
    def __init__(self, nome, idade,acordado=True):
        self.nome = nome
        self.idade = idade
        self.acordado = acordado
        
def latir(self):
    print("auau")
    
def dormir(self):
    self.acordado = False
    print("zzz")
    
    
cao_1 = ("Aladdin", "Amarelo", False)
cao_2 = ("Chappie", "Branco")

print(cao_1.acordado)
cao_1.latir()