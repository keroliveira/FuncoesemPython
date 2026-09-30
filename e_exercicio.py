# Contagem de vogais pt. 01

def contar_vogais(word):
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in word:
        if letra in vogais:
            contador += 1
    return contador

word = input()

print(f"A quantidade de vogais em {word} é {contar_vogais(word)}")