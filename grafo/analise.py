"""Item 6: conta os passos previstos pela composição de custo do capítulo.

Para `contar_triangulos`, o laço interno é o que domina:

  lista  -> para cada par (u,v) adjacente com v > u, percorre N(v): d(v) passos
  matriz -> o mesmo par custa n passos, porque `vizinhos` varre a linha inteira;
            além disso o laço externo varre n posições para cada um dos n vértices

Os dois totais são contados exatamente sobre o grafo gerado, sem executar o
laço triplo, e comparados com o tempo medido.
"""
import json
from pathlib import Path

from grafo.geracao import gerar_aleatorio
from grafo.lista import GrafoLista

N = 2000
SEMENTE = 42
DENSIDADES = [0.001, 0.05, 0.5]

tempos = {}
for linha in Path("resultados.jsonl").read_text().splitlines():
    d = json.loads(linha)
    tempos[(d["densidade_alvo"], d["implementacao"])] = d["tempo_mediano_s"]

print(f"{'delta':>7} {'m':>8} {'passos lista':>14} {'passos matriz':>14} "
      f"{'prev.':>7} {'medida':>7} {'ns/passo L':>11} {'ns/passo M':>11}")

for densidade in DENSIDADES:
    g = gerar_aleatorio(N, densidade, GrafoLista, SEMENTE)
    m = g.tamanho()
    grau = [g.grau(v) for v in range(N)]
    # passos do laço interno na lista: soma de d(v) sobre os pares (u,v), v > u
    passos_lista = sum(grau[v] * sum(1 for u in g.vizinhos(v) if u < v)
                       for v in range(N))
    passos_lista += 2 * m                     # laço do meio percorre N(u)
    passos_matriz = N * N + m * N             # varredura externa + linha por par
    prev = passos_matriz / passos_lista
    tl = tempos[(densidade, "GrafoLista")]
    tm = tempos[(densidade, "GrafoMatriz")]
    print(f"{densidade:>7} {m:>8} {passos_lista:>14,} {passos_matriz:>14,} "
          f"{prev:>7.1f} {tm/tl:>7.1f} {tl/passos_lista*1e9:>11.1f} "
          f"{tm/passos_matriz*1e9:>11.1f}")
