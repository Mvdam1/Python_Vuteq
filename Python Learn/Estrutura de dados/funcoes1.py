# codigo identado pelo nome que pode receber uma Lista de parametros

#exemplo


# def exibir_mensagem():
#     print("Este é um código identado pelo nome.")

# def exibir_mensagem1(nome = input("Nome: ")):
#    print(f"Olá,{nome}")
    
    
# def exibir_nome3(name ="Anonimo"):
#     print(f"Oláaa, {name}")
    
# #print(exibir_mensagem1())    
    
# print(exibir_nome3(name = "Cei"))
# print(exibir_mensagem())        


# print(exibir_mensagem1()) 

#Retornando valores 

# def calcular_total(numeros):
#     return sum(numeros)


# def retorna_antecessoe_e_sucessor(numero):
#     antecessor = numero - 1
#     sucessor = numero +1 
    
#     return antecessor, sucessor


# print(calcular_total([10,20,30,40,50]))

# print(retorna_antecessoe_e_sucessor(2345678987654))


#Argumentos nomeados


# def salvar_carros(marca, modelo, ano , placa):
#     print(f"Carro inserido com sucesso! {marca}, {modelo}, {ano}, {placa}")
    
# salvar_carros(marca="Ford", modelo="Mustang", ano=2020, placa="ABC-1234")
# salvar_carros(marca="Chevrolet",modelo="Onix",ano="2024",placa="9283-sdad") 

#args e kwargs
#* args **kwargs


# def exibir_poema(date_extenso,*args, **kwargs):
#     texto = "\n".join(args)
#     metadados ="\n".join([f"{chave.title():{valor}}"for chave, valor in kwargs.items()])
#     menssage =f"{date_extenso}\n\n{texto}\n\n{metadados}"
#     print(menssage)
    
# exibir_poema("20/10/2021", "Esta é uma frase", "Uma outra frase", "Uma terceira frase", data_extenso="Data: 20/10/2021", autor="Marta Martins", tema="Poema")   

#PARAMETROS ESPECIAIS