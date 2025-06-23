import pulp as p

def ler_precos():
    print("\n=== INSIRA OS PREÇOS DE VENDA ===")
    return {
        "escrivaninha": float(input("Preço da escrivaninha: ")),
        "mesa": float(input("Preço da mesa: ")),
        "armario": float(input("Preço do armário: ")),
        "prateleira": float(input("Preço da prateleira: "))
    }

def ler_coeficientes():
    print("\n=== INSIRA OS COEFICIENTES DE CONSUMO ===")
    produtos = ["escrivaninha", "mesa", "armario", "prateleira"]
    recursos = ["Tábuas", "Pranchas", "Painéis"]
    coef_restricoes = []
    for recurso in recursos:
        print(f"\n{recurso} usados por produto:")
        restricao = {}
        for prod in produtos:
            restricao[prod] = float(input(f"{prod} consome quantas {recurso}? "))
        coef_restricoes.append(restricao)
    return coef_restricoes

def ler_limites(recursos):
    print("\n=== INSIRA AS QUANTIDADES DISPONÍVEIS DE MATERIAIS ===")
    return [float(input(f"Quantidade disponível de {rec}: ")) for rec in recursos]

def resolver_otimizacao(precos, coef_restricoes, limites):
    problema = p.LpProblem("Maximizar Receita", p.LpMaximize)

    vars = {
        "escrivaninha": p.LpVariable("escrivaninha", lowBound=0),
        "mesa": p.LpVariable("mesa", lowBound=0),
        "armario": p.LpVariable("armario", lowBound=0),
        "prateleira": p.LpVariable("prateleira", lowBound=0)
    }

    problema += sum(precos[nome] * var for nome, var in vars.items())

    for i in range(3):
        problema += sum(coef_restricoes[i][nome] * var for nome, var in vars.items()) <= limites[i]

    problema.solve()

    print("\n=== SOLUÇÃO ÓTIMA ===")
    for nome in vars:
        print(f"{nome.capitalize()}: {p.value(vars[nome])}")
    print(f"Receita total: R$ {p.value(problema.objective):.2f}")

def calcular_materiais(quantidades, coef_restricoes, recursos):
    print("\n=== MATERIAIS NECESSÁRIOS PARA AS NOVAS QUANTIDADES ===")
    for i, recurso in enumerate(recursos):
        total = sum(quantidades[prod] * coef_restricoes[i][prod] for prod in quantidades)
        print(f"{recurso}: {total:.2f}")

def main():
    recursos = ["Tábuas", "Pranchas", "Painéis"]
    precos = ler_precos()
    coef_restricoes = ler_coeficientes()
    limites = ler_limites(recursos)

    resolver_otimizacao(precos, coef_restricoes, limites)

    while True:
        print("\n=== MENU ===")
        print("q - Testar novas quantidades")
        print("c - Alterar coeficientes de consumo")
        print("m - Alterar quantidade total dos materiais")
        print("p - Alterar preços dos produtos")
        print("s - Sair")

        resp = input("Escolha uma opção: ").lower()

        if resp == 's':
            print("Programa finalizado.")
            break
        elif resp == 'q':
            print("\nInforme as novas quantidades:")
            quantidades = {
                "escrivaninha": float(input("Qtd. de escrivaninha: ")),
                "mesa": float(input("Qtd. de mesa: ")),
                "armario": float(input("Qtd. de armário: ")),
                "prateleira": float(input("Qtd. de prateleira: "))
            }

            receita = sum(quantidades[prod] * precos[prod] for prod in quantidades)
            print(f"\nReceita com essas quantidades: R$ {receita:.2f}")
            calcular_materiais(quantidades, coef_restricoes, recursos)

        elif resp == 'c':
            coef_restricoes = ler_coeficientes()
            print("Coeficientes atualizados com sucesso.")
            resolver_otimizacao(precos, coef_restricoes, limites)

        elif resp == 'm':
            limites = ler_limites(recursos)
            print("Limites de materiais atualizados.")
            resolver_otimizacao(precos, coef_restricoes, limites)

        elif resp == 'p':
            precos = ler_precos()
            print("Preços atualizados com sucesso.")
            resolver_otimizacao(precos, coef_restricoes, limites)

main()
