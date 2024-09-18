nomes =["Matheus","Vinicius","De","Alexandro","Martins"]
print(nomes)
print(nomes[-2])

letras = list("Python")
print(letras)
let= input("Insira algo")
nn = list(let)
print(nn)

numeros =(list(range(10)))

#Listas aninhadas 


matriz = [
    [1,2,3],
    [3,4,5],
    [6,7,8]
    ]

print (matriz[0])#A primeira fileira inteira
print (matriz[0][0])#posição especifica
print (matriz[0][2])#Posicao especifica
print (matriz[2][2])#Posicao especifica

#fatiamento
list = ["M","i","l","e","n","a" ]
print(list[2:])# A PARTIR DO [2] ELEMENTO
print(list[:2]) #ANTES DO [2] ELEMENTO
print(list[1:3]) #dO ELEMETO[1] AO [3]
print(list[0:3:2]) #
print(list[::])#lISTA INTEIRA
print(list[::-1]) # INVERTIDA


#iterar listas 

carros =["Gol", "Celta", "Onix"]
for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"O índice {indice} possui o carro {carro}")
    
    #Filtro v1
    
numer = [1,30,99,56,76,55,4]
pares = []
impares= [numero for numero in numer if numero %2 == 1 ]

for numeros in numer:
    if numeros % 2 == 0:
        pares.append(numeros)
    print(numer)
    print(pares)
    print(impares)
    
#modificando valores

values = [2,4,6,8,10]
quadrado =[]
for numeros in values:
    quadrado.append(numeros ** 2)
print(quadrado)


#Divisão

aaaaaa =[10,20,30,40]
resultadoss =[]

for numeros in aaaaaa:
    resultadoss.append(aaaaaa * 2)
    print(resultadoss)