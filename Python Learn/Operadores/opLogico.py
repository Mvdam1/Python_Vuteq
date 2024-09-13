#operadores Logicos

#O que sao e pra que servem na linguagem

#Exemplo:


saldo = 5000
saque = 2000
limite =  1000

print(saldo >= saque and saque <= limite)

print(saldo >= saque or saque <=limite)

print (saldo <=saque and saque >=limite)

print (saldo <= saque and saque >=limite)


contato_emergencia = ["Milena"]

print(not 1000>5000)

print(not contato_emergencia)

print(not "Saque 1500")

print(not "")



#parenteses

saldo = 5000
saque = 2000
limite =  1000
conta_especial = True

print(saldo >= saque and saque <= limite or conta_especial and saldo >= saque)

print ((saldo >= saque and saque <= limite) or (conta_especial and saldo >=saque))
