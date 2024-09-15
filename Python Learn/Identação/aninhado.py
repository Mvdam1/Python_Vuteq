#Pode ter if dentroi de if 
#if ternario

saldo = 2000
saque = 100

status = "Sucesso" if saldo >= saque else "falha"

print(f"{status} ao realizar o saque")