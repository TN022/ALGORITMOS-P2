notas = {}

def adicionar_nota(aluno, nota):
    if aluno in notas:
        notas[aluno].append(nota)
    else:
        notas[aluno] = [nota]

def consultar_notas(aluno):
    if aluno in notas:
        return notas[aluno]
    else:
        return "Aluno não encontrado."

def ordenar_desempenho():
    desempenho = {}
    for aluno, notas_aluno in notas.items():
        media = sum(notas_aluno) / len(notas_aluno)
        desempenho[aluno] = media

    desempenho_ordenado = sorted(desempenho.items(), key=lambda x: x[1], reverse=True)
    return desempenho_ordenado

adicionar_nota('Joao', 8)
adicionar_nota('Maria', 7)
adicionar_nota('Joao', 6)
adicionar_nota('Maria', 9)
adicionar_nota('Pedro', 5)

print("Notas de Joao:", consultar_notas('Joao'))
print("Notas de Maria:", consultar_notas('Maria'))
print("Notas de Pedro:", consultar_notas('Pedro'))

print("\nDesempenho dos alunos:")
desempenho_ordenado = ordenar_desempenho()
for aluno, media in desempenho_ordenado:
    print(f"{aluno}: Média = {media}")
