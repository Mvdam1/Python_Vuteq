#Existem tres formas de interpolar, usando o sinal de %, a segunda é usando forma é usnado format e a terceira é usando F para poder interpolar as strings 

nome = "matheus"
idade = 19
profissao=  "Auxiliar de ti"
Linguagem = "Python"

print("Ola, me chamo %s. Eu tenho %d anos de idade, trabalho como %s, estou matriculado no curso de %s"%(nome,idade,profissao,Linguagem) )
print(f"Olá, me chamo {nome}, tenho {idade}, trabalho como {profissao}, estou matriculado no curso de {Linguagem}")
print ("Olá, me chamo {3}, tenho{2} anos de idade, trabalho como {1} e estudo {0}".format(Linguagem, profissao,idade,nome))





PI = 3,1453

print(f"O valor de PI é aproximadamente {PI:10.2f}")