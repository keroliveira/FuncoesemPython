# Quem foi aprovado?

def alunos_acima_da_media(nomes, notas):
    aprovados = []
    for i in range(len(nomes)):
        if notas[i] >= 7:
            aprovados.append(nomes[i])
    return aprovados

n = int(input())

nomes = []
notas = []
for _ in range(n):
    nome = input()
    nota = float(input())
    nomes.append(nome)
    notas.append(nota)

aprovados = alunos_acima_da_media(nomes, notas)

print("Os alunos que foram aprovados foram: ")
for nome in aprovados:
    print(nome)