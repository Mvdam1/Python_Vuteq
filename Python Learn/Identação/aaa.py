import unicodedata

def contar_vogais(s):
    # Conjunto de vogais em português (não acentuadas)
    vogais = "aeiouAEIOU"
    
    # Função para normalizar a string removendo acentos
    def remover_acentos(texto):
        # Normaliza a string para decompor caracteres acentuados em suas partes constituintes
        texto_normalizado = unicodedata.normalize('NFD', texto)
        # Remove os acentos e retorna apenas os caracteres base
        texto_sem_acentos = ''.join(c for c in texto_normalizado if not unicodedata.combining(c))
        return texto_sem_acentos

    # Remove os acentos da string de entrada
    s_normalizada = remover_acentos(s)
    
    # Contar o número de vogais na string normalizada
    contador = sum(1 for char in s_normalizada if char in vogais)
    
    return contador

def main():
    # Solicita ao usuário para inserir uma palavra
    palavra = input()
    
    # Contar o número de vogais na palavra inserida
    num_vogais = contar_vogais(palavra)
    
    # Exibir o resultado
    print(f"O número de vogais na string '{palavra}' é: {num_vogais}")

if __name__ == "__main__":
    main()
