# Atividade 3.15: Medir o Efeito da Representação de Grafos

[![Python](https://img.shields.io/badge/Python-3.14%2B-blue.svg)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/Tests-Pytest-green.svg)](https://docs.pytest.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Trabalho desenvolvido para a disciplina de **Teoria dos Grafos** do curso de Ciência da Computação da **Universidade Federal do Tocantins (UFT)**.

O projeto avalia o impacto do desempenho computacional (tempo e espaço) entre duas representações clássicas de grafos — **Matriz de Adjacência** (`GrafoMatriz`) e **Lista de Adjacência** (`GrafoLista`) — na execução do algoritmo de contagem de triângulos (`contar_triangulos`).

---

## 📌 Conteúdo e Requisitos Cobertos

- **Item 1 (Interface e Implementações):** Implementação do zero das estruturas `GrafoMatriz` e `GrafoLista` a partir de uma interface comum `Grafo`, sem dependências de bibliotecas externas (como NetworkX).
- **Item 2 (Testes de Unidade):** Verificação das propriedades estruturais n = 5, m = 6, sequência de graus (3,3,2,2,2) e teorema do aperto de mão (2m = 12) no grafo da Figura 3.1.
- **Item 3 (Matriz de Incidência):** Verificação automatizada da construção da matriz B(G) de dimensões 5x6.
- **Itens 4 e 5 (Medição de Tempo e Espaço):** Geração de grafos aleatórios de Erdos-Renyi (n = 2000) em densidades δ ∈ {0.001, 0.05, 0.5} com cálculo da mediana de tempo (3 repetições) e medição de posições de memória (n² vs n + 2m).
- **Item 6 (Análise Teórica):** Comparação quantitativa entre os passos teóricos e os tempos medidos (ns/passo), justificando o comportamento em cada densidade.
- **Item 7 (Conjunto de Dados Real):** Ingestão do dataset real `email-Eu-core` (SNAP), tratamento de laços, decomposição de arcos recíprocos e validação cruzada da contagem de triângulos (105.461).

---

## 🛠️ Estrutura do Repositório

```text
.
├── dados/
│   └── email-Eu-core.txt       # Base de dados real do SNAP
├── grafo/
│   ├── base.py                 # Interface abstrata Grafo
│   ├── matriz.py               # Representação por Matriz de Adjacência
│   ├── lista.py                # Representação por Lista de Adjacência
│   ├── geracao.py              # Gerador de grafos aleatórios (Erdos-Renyi)
│   ├── triangulos.py           # Algoritmo de contagem de triângulos
│   ├── leitura.py              # Módulo de leitura, construção e conferência
│   ├── incidencia.py           # Construção e teste da matriz de incidência (Item 3)
│   ├── medicao.py              # Benchmarks de tempo e espaço (Itens 4 e 5)
│   ├── analise.py              # Análise de passos teóricos e ns/passo (Item 6)
│   └── conjunto_real.py        # Processamento do dataset real (Item 7)
├── testes/
│   └── test_figura31.py        # Testes unitários do pytest (Item 2)
├── limpar_resultados.py        # Script utilitário para resetar resultados
├── resultados.jsonl            # Registros das medições de desempenho
├── relato-cap3.pdf             # Relatório final formatado de 1 página
└── README.md                   # Documentação do projeto
```

---

## 🚀 Como Executar

### Pré-requisitos

* Python **3.12+** instalado.
* `pytest` instalado para os testes unitários.

```bash
pip install pytest

```

### 1. Executar todos os testes e medições em comando único

No terminal (PowerShell / Linux / macOS), você pode rodar todo o pipeline sequencial de limpeza, testes, análises e medições:

```powershell
python limpar_resultados.py; pytest; python -m grafo.incidencia; python -m grafo.conjunto_real; python -m grafo.analise; python -m grafo.medicao

```

### 2. Execução Módulo a Módulo

* **Executar Testes Unitários (Item 2):**
```bash
pytest

```


* **Verificar Matriz de Incidência (Item 3):**
```bash
python -m grafo.incidencia

```


* **Executar Benchmarks de Desempenho (Itens 4 e 5):**
```bash
python -m grafo.medicao

```


* **Gerar Tabela da Análise Teórica (Item 6):**
```bash
python -m grafo.analise

```


* **Processar e Conferir Dataset Real SNAP (Item 7):**
```bash
python -m grafo.conjunto_real

```



---

## 📊 Principais Resultados

### Desempenho em Grafos Aleatórios ($n = 2000$)

| Densidade ($\delta$) | Implementação | Arestas ($m$) | Tempo Mediano (s) | Espaço (posições) | Triângulos |
| --- | --- | --- | --- | --- | --- |
| **0,001** | `GrafoMatriz` | 1.910 | ~0.33 s | 4.000.000 | 2 |
| **0,001** | `GrafoLista` | 1.910 | **~0.0008 s** | **5.820** | 2 |
| **0,05** | `GrafoMatriz` | 99.819 | ~8.97 s | 4.000.000 | 165.360 |
| **0,05** | `GrafoLista` | 99.819 | **~0.51 s** | **201.638** | 165.360 |
| **0,5** | `GrafoMatriz` | 999.109 | ~138.98 s | 4.000.000 | 166.216.758 |
| **0,5** | `GrafoLista` | 999.109 | **~49.59 s** | **2.000.218** | 166.216.758 |

### Dataset Real (`email-Eu-core`)

* **Vértices ($n$):** 986 | **Arestas ($m$):** 16.064 | **Densidade ($\delta$):** $0.03308$
* **Descartes:** 642 laços descartados (que isolaram 19 rótulos sem arestas).
* **Reciprocidade:** $8.865$ arcos recíprocos ($55,2\%$ das arestas possuem troca bidirecional).
* **Triângulos Validados:** $105.461$ (correspondência exata com o relatório oficial do SNAP).
* **Representação Indicada:** **Lista de Adjacência**, reduzindo o uso de memória em $29\times$ ($33.114$ posições contra $972.196$ da matriz) e operando com speedup de $\approx 11\times$.

---

## 👩‍💻 Autora

**Laura Barbosa Henrique**

Estudante de Ciência da Computação — *Universidade Federal do Tocantins (UFT)*

GitHub: [@tinywin](https://www.google.com/search?q=https://github.com/tinywin)

```
