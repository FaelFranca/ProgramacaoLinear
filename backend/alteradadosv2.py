import pulp as p

def ler_dados():
    print("\n=== INSIRA OS PREÇOS DE VENDA ===")
    precos = {
        "escrivaninha": float(input("Preço da escrivaninha: ")),
        "mesa": float(input("Preço da mesa: ")),
        "armario": float(input("Preço do armário: ")),
        "prateleira": float(input("Preço da prateleira: "))
    }

    print("\n=== INSIRA OS COEFICIENTES DAS VARIÁVEIS EM CADA RESTRIÇÃO ===")
    nomes = ["escrivaninha", "mesa", "armario", "prateleira"]
    coef_restricoes = []
    for i in range(3):
        print(f"Restrição {i+1}:")
        restricao = {}
        for nome in nomes:
            restricao[nome] = float(input(f"Coeficiente de {nome}: "))
        coef_restricoes.append(restricao)

    return precos, coef_restricoes

def resolver_otimizacao(precos, coef_restricoes, limites):
    problema = p.LpProblem("Maximizar Receita", p.LpMaximize)

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
    for i in range(3):
        problema += (
            coef_restricoes[i]["escrivaninha"] * escrivaninha +
            coef_restricoes[i]["mesa"] * mesa +
            coef_restricoes[i]["armario"] * armario +
            coef_restricoes[i]["prateleira"] * prateleira
            <= limites[i]
        )

    problema.solve()

    print("\n=== SOLUÇÃO ÓTIMA ===")
    print(f"Escrivaninha: {p.value(escrivaninha)}")
    print(f"Mesa: {p.value(mesa)}")
    print(f"Armário: {p.value(armario)}")
    print(f"Prateleira: {p.value(prateleira)}")
    print(f"Receita total: R$ {p.value(problema.objective):.2f}")

def calcular_restricoes_necessarias(quantidades, coef_restricoes):
    print("\n=== RESTRIÇÕES NECESSÁRIAS PARA AS NOVAS QUANTIDADES ===")
    for i, restricao in enumerate(coef_restricoes):
        total = sum(quantidades[var] * restricao[var] for var in quantidades)
        print(f"Restrição {i+1}: mínimo necessário = {total:.2f}")

def main():
    precos, coef_restricoes = ler_dados()

    limites = []
    for i in range(3):
        limites.append(float(input(f"Limite da restrição {i+1} (usar um valor qualquer para solução inicial): ")))

    resolver_otimizacao(precos, coef_restricoes, limites)

    resposta = input("\nDeseja testar outras quantidades e recalcular as restrições? (s/n): ").lower()
    if resposta == 's':
        print("\n=== INSIRA AS NOVAS QUANTIDADES DE PRODUÇÃO ===")
        quantidades = {
            "escrivaninha": float(input("Quantidade de escrivaninha: ")),
            "mesa": float(input("Quantidade de mesa: ")),
            "armario": float(input("Quantidade de armário: ")),
            "prateleira": float(input("Quantidade de prateleira: "))
        }

        receita = sum(quantidades[var] * precos[var] for var in quantidades)
        print(f"\nReceita com essas quantidades: R$ {receita:.2f}")

        calcular_restricoes_necessarias(quantidades, coef_restricoes)

main()
