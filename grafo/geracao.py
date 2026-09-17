import random
from typing import Callable

from grafo.base import Grafo


def gerar_aleatorio(
    n: int,
    densidade: float,
    criar: Callable[[int], Grafo],
    semente: int = 42,
) -> Grafo:
    """Percorre os pares u < v e insere cada um com probabilidade `densidade`.

    A semente é fixada no início, então duas chamadas com os mesmos n,
    densidade e semente produzem o mesmo grafo, mesmo que a fábrica `criar`
    seja diferente. É isso que torna a comparação entre as duas
    implementações uma comparação sobre o mesmo grafo.
    """
    random.seed(semente)
    g = criar(n)
    for u in range(n):
        for v in range(u + 1, n):
            if random.random() < densidade:
                g.inserir_aresta(u, v)
    return g
