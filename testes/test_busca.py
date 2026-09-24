"""DFS testada sobre a Figura 3.1 e checada nas duas implementações."""
from grafo.base import Grafo
from grafo.busca import componentes_conexas, dfs, dfs_floresta
from grafo.lista import GrafoLista
from grafo.matriz import GrafoMatriz

ARESTAS = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 4), (3, 4)]
IMPLEMENTACOES = [GrafoMatriz, GrafoLista]


def construir_figura31(criar) -> Grafo:
    g = criar(5)
    for u, v in ARESTAS:
        g.inserir_aresta(u, v)
    return g


def test_dfs_visita_todos_os_vertices_conexos():
    for criar in IMPLEMENTACOES:
        g = construir_figura31(criar)
        ordem, pred = dfs(g, 0)
        assert sorted(ordem) == [0, 1, 2, 3, 4]
        assert pred[0] is None
        # todo vértice, exceto a origem, tem um predecessor que é seu vizinho
        for v in ordem[1:]:
            assert g.tem_aresta(v, pred[v])


def test_dfs_arvore_tem_n_menos_1_arestas():
    for criar in IMPLEMENTACOES:
        g = construir_figura31(criar)
        _, pred = dfs(g, 0)
        arestas_da_arvore = sum(1 for v in pred if pred[v] is not None)
        assert arestas_da_arvore == g.ordem() - 1


def test_dfs_nao_depende_da_implementacao():
    ordem_matriz, _ = dfs(construir_figura31(GrafoMatriz), 0)
    ordem_lista, _ = dfs(construir_figura31(GrafoLista), 0)
    assert set(ordem_matriz) == set(ordem_lista)


def test_dfs_floresta_cobre_vertice_isolado():
    g = GrafoLista(6)  # 0..4 formam a Figura 3.1; 5 fica isolado
    for u, v in ARESTAS:
        g.inserir_aresta(u, v)
    ordem, pred = dfs_floresta(g)
    assert sorted(ordem) == [0, 1, 2, 3, 4, 5]
    assert pred[5] is None  # raiz da própria árvore, sem vizinhos


def test_componentes_conexas():
    g = GrafoLista(6)
    for u, v in ARESTAS:
        g.inserir_aresta(u, v)
    componentes = componentes_conexas(g)
    tamanhos = sorted(len(c) for c in componentes)
    assert tamanhos == [1, 5]  # {5} isolado + os outros 5 conectados


if __name__ == "__main__":
    for nome, funcao in sorted(globals().items()):
        if nome.startswith("test_"):
            funcao()
            print(f"ok  {nome}")
