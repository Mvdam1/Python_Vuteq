frutas = ("Laranja","Pera","Maça")

letras = tuple("Python",)
numeros =tuple([1,2,3,4])
pais =tuple("Brasil")


print(frutas)
print(frutas[2])
print(letras)
print(numeros)
print(pais)

#tUPLAS ANINHADAS 

matriz =(
    
    (1,'a',2),
    (3,'b',4),
    (5,'c',6)
    
)
print(matriz[2])
print(matriz[2][1])
print(matriz[2][-1])


#fatiamento



tupla =("p","y","t","h","o","n")

print(tupla[2:]) # A PARTIR DO [2] ELEMENTO
print(tupla[:2]) #Só os dois primeiros elemtentos   
print(tupla[1:3]) #do numero um ao 3
print(tupla[::]) #TUdo
print(tupla[::-1]) # inverso 


#Iterar tupla

carros =("Gol","Celta","Astra")

for carro in carros:
    print(carro)
    
    
for indice, carro in enumerate(carro):
    print(f"O índice {indice} possui o carro {carro}")
    

#().count()

cores = ("vermelho","Branco")
cores.count("vermelho")
print(cores)
print(cores.count("vermelho"))



#Index 
linguagens =('pythons','java','c#')

print(linguagens.index('pythons'))


#Len
print('Aqui é Len com a variavel Linguagens')
print(len(linguagens))


carr = ("gol")
print(isinstance(carros, tuple))
