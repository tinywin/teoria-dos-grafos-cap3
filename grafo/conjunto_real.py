"""Item 7: lê um conjunto real com o pipeline do capítulo e confere o resultado.

Conjuntos orientados fazem o par (v,u) chegar a `construir`
como repetição do par (u,v). Este script separa o contador `repetidas` em duas
parcelas de origem distinta, como o enunciado pede.
"""
from pathlib import Path

from grafo.conferencia import conferir
from grafo.construcao import construir
from grafo.leitura import indexar, ler_pares
from grafo.lista import GrafoLista

import sys

from grafo.triangulos import contar_triangulos

ARQUIVO = Path(sys.argv[1] if len(sys.argv) > 1 else "dados/email-Eu-core.txt")
print(f"arquivo: {ARQUIVO}\n")

pares, relatorio = ler_pares(ARQUIVO)
indice = indexar(pares)
g, repetidas = construir(pares, indice, GrafoLista)
medidas = conferir(g)

# rótulos distintos no arquivo inteiro, inclusive os que só aparecem em laço
rotulos = set()
for numero, linha in enumerate(ARQUIVO.read_text().splitlines(), start=1):
    linha = linha.strip()
    if not linha or linha.startswith("#"):
        continue
    campos = linha.split()
    rotulos.update(campos[:2])

# decomposição do contador `repetidas`
ordenados = {(u, v) for u, v in pares}
mesmo_sentido = len(pares) - len(ordenados)          # mesma mensagem par->par de novo
reciprocos = len(ordenados) - g.tamanho()            # (v,u) quando (u,v) já existia

print("--- leitura ---")
print(f"linhas do arquivo:        {relatorio['linhas']}")
print(f"linhas ignoradas:         {relatorio['ignoradas']}")
print(f"laços descartados:        {relatorio['lacos']}")
print(f"pares entregues:          {len(pares)}")
print()
print("--- grafo ---")
print(f"n (ordem):                {medidas['n']}")
print(f"rótulos distintos:        {len(rotulos)}")
print(f"m (tamanho):              {medidas['m']}")
print(f"soma dos graus:           {medidas['soma_graus']}")
print(f"aperto de mão:            {medidas['aperto_de_mao']}")
print(f"vértices isolados:        {medidas['isolados']}")
print(f"densidade:                {medidas['densidade']:.6f}")
print()
print("--- decomposição de `repetidas` ---")
print(f"repetidas (total):        {repetidas}")
print(f"  mesmo sentido (u,v):    {mesmo_sentido}")
print(f"  arco recíproco (v,u):   {reciprocos}")
print(f"pares ordenados distintos:{len(ordenados)}")
print()
print("--- espaço, se o grafo fosse guardado nas duas estruturas ---")
n, m = medidas["n"], medidas["m"]
print(f"matriz  n^2   = {n*n:,}")
print(f"lista   n+2m  = {n + 2*m:,}")
print(f"razão         = {n*n / (n + 2*m):.1f}x")
print()
print("--- conferência independente ---")
print(f"triângulos (contar_triangulos): {contar_triangulos(g):,}")
