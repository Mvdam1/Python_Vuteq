#Funcionamento e estrutura de dados em python z

#Crianco SETS
#Set é uma coleção que nao possui objetos repetidos
#Usa-se sets para representar conjuntos matematicos ou eliminar itens duplicados de um iteravel

numb=set([1,2,3,4,5,6,7,8,9,10])
letas=set("Abacaxi") #{a,b,a,c,x,i}
carros=set(("palio","Gol","Celta")) #{"palio","Gol","Celta"}

numeros =list(numb)

print(numeros)
print(carros)
print(letas)
print(numb)


#funcao enumerate

for indice, carro in enumerate(carros):
    print(f"O índice {indice} possui o carro {carro}")
    
    
 #metodos da classe set

#union
conjunto_a = {1,2,3}
conjunto_b = {3,4},5;

conjunto_a.union(conjunto_b)

#intersection

conjunto_a.intersection(conjunto_b)


#Dference 

conjunto_a.difference(conjunto_b)
conjunto_b.difference(conjunto_a)


#symmetric_difference

conjunto_a.symmetric_difference(conjunto_b)

#issubset 
conjunto_a.issubset(conjunto_b)
conjunto_b.issubset(conjunto_a)

#issuperset

conjunto_b.issuperset(conjunto_a)

#isdisjoint

conjunto_c = {1,0}

conjunto_a.isdisjoint(conjunto_b) #True
conjunto_a.isdisjoint(conjunto_c) #False

#ADD

sorteio = {1,23}
sorteio.add(21)
#{1,23,21}

#clear
sorteio #{1.23}
sorteio.clear()
sorteio #{}

#copy

sorteio #{1.23}
sorteio.copy()
sorteio #{1,23}

#Discard

Numerooos = {1,2,3,4,5,6,7,8,9,10,11,12,13}

Numerooos.discard(5)    #O numero que estiver dentro do parenteses sera o numero removido 

len(Numerooos)

#IN 
1 in Numerooos # RETORNA A CONDIÇÃO SE VERDADEIRO OU FALSO
2 in Numerooos


