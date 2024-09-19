#Estrutura base di dicionario 

#Criação do acesso ao dicionario 

#Dicionario é um conjunto nao ordenado  de pares chave:valor, onde as chaves são unicas em dada instancia
#do dicionario. São delimitados por chaves {} e contem uma lista de pares chave: valor separado pro virgula



pessoa1 ={"nome":"Matheus","idade":19}
pessoa =dict (nome="Matheus",Idade=19) 
pessoa["Telefone"]="33333333333"
pessoa["nome"] = "Vinicius"

print (pessoa1)
print (pessoa)

#dicionarios aninhados 

contatos ={
    "Matheus":{
        "Telefone":"33333333333",
        "Email":"matheus@gmail.com"
    },
    "Vinicius":{
        "Telefone":"99999999999",
        "Email":"vinicius@gmail.com"
    },
    "Milena":{
        "Nome":"Milena Yamaute",
        "Telefone":"77777777777",
        "Email":"milena@gmail.com"
    }
}
print(contatos["Milena"])

pessoa["nome"] = "Martins"
print(pessoa)





for chave in contatos:
    print(chave,contatos[chave])
    
    
    
for key,valor in contatos.items():
    print(key,valor)
    
    
#metodos da classe dicionario 
#metodo copy

copia= contatos.copy()
copia["milena"] = {"nome":"Amor"}
print(copia["milena"]["nome"])





#Metodos CLear

##print(f"Existem os seguintes contatos: \n{contatos}")


#Fromkey

dict.fromkeys(["nome","telefone"])
dict.fromkeys(["telefone","nome"],"vazios")   

#Get

# contatos["chave"] #keyerror
# contatos.get("chave")
# contatos.get("chave",{})
# contatos.get("Matheus",{})
# print(contatos)

#item 
print(contatos.items())

#retorna lista de tuplas

#keys retorna as chaves do dicionario 

print(contatos.keys())

#pop remove um valor do dicionario 

print   (contatos.pop("Joao","Not found"))
contatos.pop("Matheus")
print(contatos)

#Set default
#Se o valor existir, ele nao altera , se nao existir, ele acrescenta 


baba ={"nome":"Jonas","idade":10}

baba.setdefault("idade",50)
print(baba)

baba.setdefault("peso",60)
print(baba)

#update
#atualização do dicionario

baba.update({"peso":55})
print(baba)

baba.update({"idade":11})
print(baba) 

baba.update({"mãe":"lucia","pai":"Joao"})
print(baba)
baba.update({"Irmao":"Matheus"})
#values, retorna os valores
print(baba)
print(baba.values())

#in 
resposta = "Irmao" in baba 
print(resposta) #false


#Del

del baba["mãe"]
print(baba)

