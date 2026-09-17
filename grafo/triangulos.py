import sys
from pathlib import Path

PROJETO_DIR = Path(__file__).resolve().parent.parent
if str(PROJETO_DIR) not in sys.path:
    sys.path.insert(0, str(PROJETO_DIR))

from grafo.base import Grafo


def contar_triangulos(g: Grafo) -> int:
    """Conta o número de triângulos no grafo.
    
    Para evitar contar o mesmo triângulo {u, v, w} múltiplas vezes,
    impomos a restrição de ordem estrita: u < v < w.
    """
    total = 0
    for u in g.vertices():
        for v in g.vizinhos(u):
            if v <= u:
                continue
            for w in g.vizinhos(v):
                # Para garantir u < v < w sem depender apenas de v < w:
                if w <= v or w <= u:
                    continue
                if g.tem_aresta(u, w):
                    total += 1
    return total