#Quando utilizar
#For e While;

#exemplo sem repetição;

a = int(input("Informe numeros inteiros: "))

a+= 1 
print (a)

a+= 1 
print(a)


#For

texto = input("Informe o texto: ")

VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print()


#FOR/ELSE

#texto = input("Informe o texto: ")
texto =""
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:#nao muito comum no dia a dia 
    print()
    print("EXecuta no final do laço")


#funcao build in range, usadoi para produzirr uma sequenciaa de numeros inteiros a partider de um inicio inclusivo para um fim exclusivo
#i,i+2,i+3

#range(stop) -> range object
#range (start,stop[, step]) -> range object

list(range(4))
print(list(range(10)))


#Utilizando com for



#for numero in range(0,11):
 ##       print(numero, end=' ')


#exibindo a tabuada do 9

for numero in range(0,82,9):
     print(numero, end=" ")
     


#While (Executar ate que algo aconteça!!!!!!!)
#Uitlizar ate que uma condição aconteça

opcao = -1

while opcao !=0:
    opcao= int(input("[1]Sacar \n[2] Extrato \n[0]Sair \n"))

if opcao ==1:
    print("sacando!")
elif opcao == 2 :
    print("extrato")
