"""Item 3: matriz de incidência da Figura 3.1, escrita à mão e conferida.

A numeração das arestas segue a figura:
e1 = v1v2, e2 = v1v3, e3 = v2v3, e4 = v2v4, e5 = v3v5, e6 = v4v5.
As linhas são os vértices v1..v5 e as colunas são as arestas e1..e6.
"""

B = [
    [1, 1, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0],
    [0, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 1],
]

GRAUS_ESPERADOS = [2, 3, 3, 2, 2]


def somas_das_colunas(b: list[list[int]]) -> list[int]:
    return [sum(linha[j] for linha in b) for j in range(len(b[0]))]


def somas_das_linhas(b: list[list[int]]) -> list[int]:
    return [sum(linha) for linha in b]


def conferir_incidencia(b: list[list[int]], graus: list[int]) -> None:
    colunas = somas_das_colunas(b)
    assert all(s == 2 for s in colunas), f"coluna com soma diferente de 2: {colunas}"
    linhas = somas_das_linhas(b)
    assert linhas == graus, f"linhas {linhas} não batem com os graus {graus}"


if __name__ == "__main__":
    conferir_incidencia(B, GRAUS_ESPERADOS)
    print("somas das colunas:", somas_das_colunas(B))
    print("somas das linhas: ", somas_das_linhas(B))
    print("graus esperados:  ", GRAUS_ESPERADOS)
    print("total:", sum(somas_das_linhas(B)), "= 2m =", 2 * len(B[0]))
    print("ok  toda coluna soma 2 e a linha i soma d(vi)")
