import pulp as p

receitaVenda = p.LpProblem('Problema', p.LpMaximize)

#Variaveis
escrivaninha = p.LpVariable("escrivaninha", lowBound = 0)
mesa = p.LpVariable("mesa", lowBound = 0)
armario = p.LpVariable("armario", lowBound = 0)
prateleira = p.LpVariable("prateleira", lowBound = 0)

#Sujeito a:
receitaVenda += 100 * escrivaninha + 80 * mesa +  120 * armario + 20 * prateleira

#Variaveis
receitaVenda += escrivaninha + mesa + armario + 4 * prateleira <= 250
receitaVenda += mesa + armario + 2 * prateleira <= 600
receitaVenda += 3 * escrivaninha + 2 * mesa + 4 * armario <= 500 

#print (receitaVenda)

#Solver
status = receitaVenda.solve()
#Solucoes 
#print(p.LpStatus[status])

#Resultados
print(f"Escrivaninha: {p.value(escrivaninha)}")
print(f"Mesa: {p.value(mesa)}")
print(f"Armário: {p.value(armario)}")
print(f"Prateleira: {p.value(prateleira)}")
print(f"Receita total: {p.value(receitaVenda.objective)}")

