class Bicicleta:
    def __init__(self,cor,modelo,ano,valor):
     self.cor= cor
     self.modelo= modelo
     self.ano = ano     
     self.valor= valor
     self.marcha = 1
     
    def trocar_marcha(self, nro_marcha):
        print(nro_marcha)
        print ("marcha trocada")
        _self = self
        
    def trocar_marcha(self, nro_marcha):
        
         if nro_marcha > self.marcha:
             print("Marcha troca")
         else:
             print("Marcha não pode ser trocada para esta marcha")
             return

    def parar (self):
            print("plim")
            print("Estou parando!")    
    
    
    def buzinar(self):
        print("piiiii")
    
    
    def correr(self):
        print("Vrummm")
        
    # def __str(self):
    #     return f"Bicicleta : {self.cor}, {self.modelo}, {self.ano}, {self.valor},"
    
    def __str__(self):
        return f"{self.__class__.__name__}: {[f"{chave} = {valor}" for chave , valor in self.
    __dict__.items()  ]} "
    
b1 = Bicicleta("Vermelha","Caloi",2022,600)
b2 = Bicicleta("Azul","Monark",2020,900)  
#b1.trocar_marcha()

b1.parar()    
b1.correr()
print(b1.cor, b1.ano)
b2.correr() 
Bicicleta.correr(b1)

print(b2)