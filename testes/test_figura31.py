"""Item 2: constrói o grafo da Figura 3.1 nas duas implementações e confere.

Os vértices v1..v5 da figura correspondem aos índices 0..4, seguindo a
convenção da interface (vértices 0, 1, ..., n-1).
"""
from grafo.base import Grafo
from grafo.lista import GrafoLista
from grafo.matriz import GrafoMatriz

ARESTAS = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 4), (3, 4)]
IMPLEMENTACOES = [GrafoMatriz, GrafoLista]


def construir_figura31(criar) -> Grafo:
    g = criar(5)
    for u, v in ARESTAS:
        g.inserir_aresta(u, v)
    return g


def test_ordem():
    for criar in IMPLEMENTACOES:
        assert construir_figura31(criar).ordem() == 5


def test_tamanho():
    for criar in IMPLEMENTACOES:
        assert construir_figura31(criar).tamanho() == 6


def test_sequencia_de_graus():
    for criar in IMPLEMENTACOES:
        g = construir_figura31(criar)
        graus = sorted((g.grau(v) for v in g.vertices()), reverse=True)
        assert graus == [3, 3, 2, 2, 2]


def test_aperto_de_mao():
    for criar in IMPLEMENTACOES:
        g = construir_figura31(criar)
        soma = sum(g.grau(v) for v in g.vertices())
        assert soma == 2 * g.tamanho()


def test_as_duas_implementacoes_concordam():
    matriz = construir_figura31(GrafoMatriz)
    lista = construir_figura31(GrafoLista)
    for u in range(5):
        assert sorted(matriz.vizinhos(u)) == sorted(lista.vizinhos(u))


if __name__ == "__main__":
    for nome, funcao in sorted(globals().items()):
        if nome.startswith("test_"):
            funcao()
            print(f"ok  {nome}")
