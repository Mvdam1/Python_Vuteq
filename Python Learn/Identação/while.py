#While (Executar ate que algo aconteça!!!!!!!)
#Uitlizar ate que uma condição aconteça

opcao = -1

while opcao !=0:
    opcao= int(input("[1]Sacar \n[2] Extrato \n[0]Sair \n: "))

    if opcao == 1:
        print("sacando!")   
    
    elif opcao == 2 :
        print("extrato")
#else
else:
    print("Obrigado por usar nosso sistema")


#Estrutura de repetição BREAK

opcao = -1

while opcao != 0:
    opcao(int(input("Informe o numero")))
        