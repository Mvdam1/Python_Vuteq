class Veiculo:
    def __init__(self,cor,modelo,nome,rodas):
        self.cor = cor
        self.modelo = modelo
        self.nome = nome
        self.rodas = rodas

    def ligas_motor(self):
        print("engine strart")
    def freiar(self):
        print("Freios acionados")
        
    def acelerar(self):
        print("Acelerando")
        
        
        
class Carro(Veiculo):
    pass

class Moto(Veiculo):
    pass

class Caminhão(Veiculo):
    def __init(self,cor,modelo,nome,rodas,carregado):
        super().__init__(cor,modelo,nome,rodas,carregado)
        self.carregado = carregado
        
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'}estou carregado")
        

moto = Moto("Fazer","Preta","Moto carenada","ABCD123")
moto.ligas_motor()
moto.acelerar()
moto.freiar()