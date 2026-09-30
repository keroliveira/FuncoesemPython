# Contagem de vogais pt. 02

def contar_vogais(word):
    vogais = "aeiou"
    contagem = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    for letra in word.lower():
        if letra in vogais:
            contagem[letra] += 1
    
    return contagem

word = input()

print(contar_vogais(word))