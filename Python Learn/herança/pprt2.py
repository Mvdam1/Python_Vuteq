class Pessoa:
    def __init__(self, nome,ano_nascimento):
        self.nome = nome
        self.ano_nascimento = ano_nascimento        
    @property
    def nome(self):
        return self.nome
    
    @nome.setter
    def nome(self, value):
        #logica para modificar o nome
    
        @property
        def idade(self):
            _ano_atual = 2024
            return _ano_atual - self.ano_nascimento 

    def get_nome(self):
        return self.nome
    
    def get_idade(self):
        return 2024 - self.ano_nascimento
    
    
    
pessoa = Pessoa("Matheus",2004)

print (f"Nome:{pessoa.nome} \t Idade:{pessoa.idade}")