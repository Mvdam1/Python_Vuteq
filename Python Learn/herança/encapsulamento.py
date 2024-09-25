#Proteção dos dados da herança , para evitar modificações aos dados de forma acidental 
#Recursos publicos e privados , em python se usa conenção 
#Definição : Publico : Pode ser acessado de fora da classe, Privado : Pode ser acessado somente pela classe 

#Todos os recursos sao publicos, desde que nao comecem com underlinde 
#ex

class Conta:
    def __init__(self,nro_agencia, saldo = 0 ):
        self.saldo = saldo
        self.nro_agencia = nro_agencia
        
    def Depositar(self,valor):
        self.saldo += valor
    
    def Sacar(self,valor):
        self.saldo -= valor
    
    def mostrar_saldo(self):
        return self.saldo


conta = Conta("0001",100)
#conta.Sacar(10)
conta.Depositar(200)
print(conta.saldo)
print(conta.nro_agencia)
