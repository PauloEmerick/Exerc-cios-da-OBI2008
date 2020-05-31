print("QUESTÃO 01")
def qtd_competidores(N, P, lista):
    a = 0
    for c in range(N):
        competidor = lista[c]
        fase1 = competidor[0]
        fase2 = competidor[1]
        totalidade = fase1 +fase2
        if totalidade >= P:
            a += 1
    return a

print(qtd_competidores (4, 235, [(100,134),(0,0),(200,200),(150,150)]))
