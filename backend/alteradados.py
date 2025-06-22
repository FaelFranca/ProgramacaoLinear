import pulp as p

def ler_dados():
    print("=== INSIRA OS PREÇOS DE VENDA ===")
    precos = {
        "escrivaninha": float(input("Preço da escrivaninha: ")),
        "mesa": float(input("Preço da mesa: ")),
        "armario": float(input("Preço do armário: ")),
        "prateleira": float(input("Preço da prateleira: "))
    }

    print("\n=== INSIRA OS LIMITES DAS RESTRIÇÕES ===")
    limites = [
        float(input("Limite da restrição 1: ")),
        float(input("Limite da restrição 2: ")),
        float(input("Limite da restrição 3: "))
    ]

    print("\n=== INSIRA OS COEFICIENTES DAS VARIÁVEIS EM CADA RESTRIÇÃO ===")
    nomes = ["escrivaninha", "mesa", "armario", "prateleira"]
    coef_restricoes = []
    for i in range(3):
        print(f"Restrição {i+1}:")
        restricao = {}
        for nome in nomes:
            restricao[nome] = float(input(f"Coeficiente de {nome}: "))
        coef_restricoes.append(restricao)

    return precos, limites, coef_restricoes

def resolver_otimizacao(precos, limites, coef_restricoes):
    problema = p.LpProblem("Maximizar Receita", p.LpMaximize)

    # Variáveis
    escrivaninha = p.LpVariable("escrivaninha", lowBound=0)
    mesa = p.LpVariable("mesa", lowBound=0)
    armario = p.LpVariable("armario", lowBound=0)
    prateleira = p.LpVariable("prateleira", lowBound=0)

    # Objetivo
    problema += (
        precos["escrivaninha"] * escrivaninha +
        precos["mesa"] * mesa +
        precos["armario"] * armario +
        precos["prateleira"] * prateleira
    )

    # Restrições
    problema += (
        coef_restricoes[0]["escrivaninha"] * escrivaninha +
        coef_restricoes[0]["mesa"] * mesa +
        coef_restricoes[0]["armario"] * armario +
        coef_restricoes[0]["prateleira"] * prateleira
        <= limites[0]
    )
    
    problema += (
        coef_restricoes[1]["escrivaninha"] * escrivaninha +
        coef_restricoes[1]["mesa"] * mesa +
        coef_restricoes[1]["armario"] * armario +
        coef_restricoes[1]["prateleira"] * prateleira
        <= limites[1]
    )
    
    problema += (
        coef_restricoes[2]["escrivaninha"] * escrivaninha +
        coef_restricoes[2]["mesa"] * mesa +
        coef_restricoes[2]["armario"] * armario +
        coef_restricoes[2]["prateleira"] * prateleira
        <= limites[2]
    )

    # Resolver
    problema.solve()

    # Resultados
    print("\n=== RESULTADOS ===")
    print(f"Escrivaninha: {p.value(escrivaninha)}")
    print(f"Mesa: {p.value(mesa)}")
    print(f"Armário: {p.value(armario)}")
    print(f"Prateleira: {p.value(prateleira)}")
    print(f"Receita total: {p.value(problema.objective)}")

# Programa principal
precos, limites, coef_restricoes = ler_dados()
resolver_otimizacao(precos, limites, coef_restricoes)
