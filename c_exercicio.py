# Qual é a área?

def area_retangulo(base, altura):
    return base * altura

base = float(input())
altura = float(input())

area = area_retangulo(base, altura)

print(f"A área do retângulo é {area:.2f}")