"""Busca em profundidade (DFS) sobre a interface `Grafo`.

Segue o mesmo estilo do capítulo: interface única (`Grafo.vizinhos`), sem
depender de qual implementação (lista ou matriz) está por trás.

A versão é iterativa (pilha explícita), não recursiva: para um grafo real
como email-Eu-core (milhares de vértices em cadeia), uma DFS recursiva pode
estourar o limite de recursão do Python. A pilha guarda, para cada vértice
aberto, um iterador sobre seus vizinhos ainda não consumidos — assim cada
vértice é "retomado" de onde parou, exatamente como a recursão faria.
"""
from typing import Iterator

from grafo.base import Grafo


def dfs(g: Grafo, origem: int) -> tuple[list[int], dict[int, int | None]]:
    """DFS a partir de `origem`, alcançando só a componente de `origem`.

    Devolve (ordem, pred):
      ordem: vértices na ordem em que foram descobertos (pai antes do filho).
      pred:  predecessor de cada vértice visitado na árvore de busca;
             pred[origem] é None.

    A pilha guarda pares (vértice aberto, iterador de seus vizinhos), para
    que cada vértice seja retomado de onde parou quando o topo da pilha
    volta a ele — o mesmo papel que a pilha de chamadas teria numa DFS
    recursiva.
    """
    pred: dict[int, int | None] = {origem: None}
    ordem = [origem]
    pilha: list[tuple[int, Iterator[int]]] = [(origem, iter(g.vizinhos(origem)))]

    while pilha:
        pai, vizinhos = pilha[-1]
        avancou = False
        for v in vizinhos:
            if v not in pred:
                pred[v] = pai
                ordem.append(v)
                pilha.append((v, iter(g.vizinhos(v))))
                avancou = True
                break
        if not avancou:
            pilha.pop()

    return ordem, pred


def dfs_floresta(g: Grafo) -> tuple[list[int], dict[int, int | None]]:
    """DFS sobre todos os vértices, cobrindo grafos desconexos.

    Percorre os vértices em ordem 0..n-1 e dispara uma nova DFS a cada
    vértice ainda não visitado, formando uma floresta de busca. Devolve a
    ordem global de descoberta e o predecessor de cada vértice (None para
    a raiz de cada árvore da floresta).
    """
    visitado: set[int] = set()
    pred: dict[int, int | None] = {}
    ordem: list[int] = []

    for raiz in g.vertices():
        if raiz in visitado:
            continue
        pred[raiz] = None
        visitado.add(raiz)
        ordem.append(raiz)
        pilha: list[tuple[int, Iterator[int]]] = [(raiz, iter(g.vizinhos(raiz)))]
        while pilha:
            pai, vizinhos = pilha[-1]
            avancou = False
            for v in vizinhos:
                if v not in visitado:
                    visitado.add(v)
                    pred[v] = pai
                    ordem.append(v)
                    pilha.append((v, iter(g.vizinhos(v))))
                    avancou = True
                    break
            if not avancou:
                pilha.pop()

    return ordem, pred


def componentes_conexas(g: Grafo) -> list[list[int]]:
    """Uma lista de componentes (cada uma como lista de vértices), via DFS."""
    _, pred = dfs_floresta(g)
    raiz_de: dict[int, int] = {}

    def raiz(v: int) -> int:
        caminho = []
        while pred[v] is not None:
            caminho.append(v)
            v = pred[v]
        for u in caminho:
            raiz_de[u] = v
        return v

    grupos: dict[int, list[int]] = {}
    for v in g.vertices():
        r = raiz(v)
        grupos.setdefault(r, []).append(v)
    return list(grupos.values())
