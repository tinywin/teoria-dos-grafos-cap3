"""Itens 4 e 5: gera os grafos aleatórios e mede tempo e espaço.

Uso:
    python -m grafo.medicao                 # roda todas as configurações
    python -m grafo.medicao 0.5 GrafoLista  # roda uma configuração só

Cada configuração medida é acrescentada a resultados.jsonl.
"""
import json
import statistics
import sys
import time
from pathlib import Path

from grafo.geracao import gerar_aleatorio
from grafo.lista import GrafoLista
from grafo.matriz import GrafoMatriz
from grafo.triangulos import contar_triangulos

N = 2000
SEMENTE = 42
REPETICOES = 3
DENSIDADES = [0.001, 0.05, 0.5]
IMPLEMENTACOES = {"GrafoMatriz": GrafoMatriz, "GrafoLista": GrafoLista}
SAIDA = Path("resultados.jsonl")


def medir(g) -> tuple[float, int]:
    """Executa contar_triangulos REPETICOES vezes e devolve a mediana."""
    tempos = []
    for rep in range(1, REPETICOES + 1):
        print(f"   └─ Executando repetição {rep}/{REPETICOES}...", end="", flush=True)
        inicio = time.perf_counter()
        triangulos = contar_triangulos(g)
        duracao = time.perf_counter() - inicio
        tempos.append(duracao)
        print(f" concluído em {duracao:.2f}s", flush=True)
    return statistics.median(tempos), triangulos


def executar(densidade: float, nome: str) -> dict:
    print(f"-> Gerando grafo aleatório (n={N}, delta={densidade}, impl={nome})...", flush=True)
    g = gerar_aleatorio(N, densidade, IMPLEMENTACOES[nome], SEMENTE)
    m = g.tamanho()
    print(f"   Arestas geradas: {m:,}. Iniciando medições...", flush=True)
    tempo, triangulos = medir(g)
    return {
        "densidade_alvo": densidade,
        "implementacao": nome,
        "n": g.ordem(),
        "m": m,
        "densidade_obtida": 2 * m / (N * (N - 1)),
        "tempo_mediano_s": tempo,
        "espaco_posicoes": g.posicoes(),
        "triangulos": triangulos,
        "repeticoes": REPETICOES,
        "semente": SEMENTE,
    }


def main(argv: list[str]) -> None:
    if len(argv) == 2:
        casos = [(float(argv[0]), argv[1])]
    else:
        casos = [(d, nome) for d in DENSIDADES for nome in IMPLEMENTACOES]
    
    total_casos = len(casos)
    for idx, (densidade, nome) in enumerate(casos, start=1):
        print(f"\n[{idx}/{total_casos}] Medição de desempenho", flush=True)
        linha = executar(densidade, nome)
        print(f"-> Resultado obtido (tempo mediano: {linha['tempo_mediano_s']:.4f}s):", flush=True)
        print(json.dumps(linha), flush=True)
        with SAIDA.open("a", encoding="utf-8") as arquivo:
            arquivo.write(json.dumps(linha) + "\n")


if __name__ == "__main__":
    main(sys.argv[1:])