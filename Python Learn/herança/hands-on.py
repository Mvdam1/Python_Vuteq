class Veiculo:
    def __init__(self,cor,modelo,nome,rodas):
        self.cor = cor
        self.modelo = modelo
        self.nome = nome
        self.rodas = rodas

    def ligas_motor(self):
        print("engine strart")

        
        
        
class Carro(Veiculo):
    pass

class Moto(Veiculo):
    pass

class Caminhão(Veiculo):
    pass

moto = Moto("Fazer","Preta","Moto carenada","ABCD123")
print(moto.cor)