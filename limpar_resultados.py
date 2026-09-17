import json

LINHAS_UNICAS = {}

# Lê o arquivo e guarda apenas a última medição de cada combinação
with open("resultados.jsonl", "r", encoding="utf-8") as f:
    for linha in f:
        linha_str = linha.strip()
        if not linha_str:
            continue
        dado = json.loads(linha_str)
        chave = (dado["densidade_alvo"], dado["implementacao"])
        LINHAS_UNICAS[chave] = dado

# Reescreve o arquivo limpo
with open("resultados.jsonl", "w", encoding="utf-8") as f:
    for dado in LINHAS_UNICAS.values():
        f.write(json.dumps(dado) + "\n")

print(f"Arquivo resultados.jsonl limpo com sucesso! Restaram {len(LINHAS_UNICAS)} entradas.")