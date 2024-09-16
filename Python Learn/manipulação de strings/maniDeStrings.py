#conhecendo os metodos uteis de strjngs 


nome = "matheus"

print(nome.upper())
print(nome.lower())
print(nome.title())


texto = f"Olá, meu nome é {nome} eu tenho dezenove anos      "
print(texto)
print(texto.strip()+ '...')
print(texto.lstrip() +'...')
print(texto.rstrip() +'...')

menu ="python " 
print("###" + menu +"###")
print("###" + menu +"###")
print(menu.center(14))
print(menu.center(14,'#'))
print("p-y-t-h-o-n")

for letra in menu:
    print(letra,end="-")
print();
print('-'.join(menu))

