lista = []
lista.append(1)
lista.append("Python")
lista.append([10,20,30,40])
print(lista)
#lista.clear()
print(lista)
l2 = lista.copy()
print(l2)

print(id(l2), id(lista))



cores = ["preto","amarelo","vermelho","azul"]

print(cores.count("preto"))
print(cores.count("amarelo"))
print(cores.count("vermelho"))
print(cores.count("azul"))

#extend

linguagens = ["Java","C","Python","JavaScript","Ruby"]
print(linguagens)
linguagens.extend(["Rust","C++"])
print(linguagens)
print(linguagens[2])

#Indexing
print(linguagens.index("Java"))
print(linguagens.index("Python"))
print(linguagens.index("Rust"))

#pop

print(linguagens.pop())
print(linguagens)

print(linguagens.pop(1))
print(linguagens)

#REMOVE

linguagens.remove("Java")
print(linguagens)

linguagens.remove("JavaScript")
print(linguagens)

#reverse
linguagens.reverse()
print(linguagens)

#LEN

len(linguagens)
print(len(linguagens))


