def contador_vogais(string):
    result = 0
    string = string.lower()
    vogais = "aeiou"
    for i in vogais:
        result += string.count(i)   
    return(f"O número de vogais na string 'Python' é: {result}")
print (contador_vogais("Python"))
    