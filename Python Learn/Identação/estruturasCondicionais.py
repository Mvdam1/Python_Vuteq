#Estruturas condicionais e como sao utilizados em python ( if/else/elif)
#if aninhado e if ternario


#Permitem o desvio de fluxo de controle quando determinadas expressões logicas sao atendidas

#idade = int(input("digite sua idade: "))

#if idade >=18:
 #   print("Voce pode tirar sua carta")
#else:
 #   print("Voce nao pode tirar sua carta!")
#IF ELIF ELSE

"""
saldo = 2500.0
limite = 1000.0

saque = float(input("Insira o valor que deseja sacar: "))
resto = saldo - saque
print(resto)

if saldo >= saque and limite <= saque :
    print("Voce tem saldo mas nao pode sacar")


else:
    print(f"Foi retirado o valor de {saque} , sobraram {resto}")





"""


extrato = 25000
opcao = int(input("Selecione uma opção: [1]Sacar:  \n[2] Extrato: "))

if opcao == 1:
    
    Valor = int(input("Informe a quantia do saque:"))
    sobra = extrato - Valor
    print(f"Foi retirado {Valor}, e sobraram {sobra}...")


elif opcao ==2:
    print(f"Exibindo extrato...{extrato}")

else:
    SystemExit("Opção invalida") 


