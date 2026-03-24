import pandas  as pd
import numpy as np
import matplotlib as plt

# (a) Definição da semente global e geração da instância.
n = 20 # Numero Total de Itens
np.random.seed(42)

w = np.random.randint(1, 16, size=n) 
v = np.random.randint(1, 21, size=n)
Capacidade = np.sum(w)/2

print("---------------- Instância Gerada ----------------\n")
print(f"Pesos (w) = {w}")
print(f"Valores (v) = {v}")
print(f"Capacidade = {Capacidade}")
print("\n--------------------------------------------------\n")


# (b) Busca Aleatória Pura
repeticoes = 30
amostras = 10**4
resultados = []
melhores_solucoes = []

for semente in range(repeticoes):
  np.random.seed(semente)

  melhor_resultado = 0
  melhor_solucao = 0

  solucoes = np.random.randint(0, 2, size=(amostras, n))

  for solucao in solucoes:
    peso_solucao = np.dot(solucao, w)
  
    if peso_solucao <= Capacidade:
      valor_solucao = np.dot(solucao, v)

      if valor_solucao > melhor_resultado:
        melhor_resultado = valor_solucao
        melhor_solucao = solucao

  resultados.append(melhor_resultado)
  melhores_solucoes.append(melhor_solucao)

indice_maior = np.argmax(resultados)

print("--------------- Busca Aleatória Pura ---------------\n")
print(f"Melhores Resultados: {(resultados)}\n")

print(f"Melhor Solução obtida : {melhores_solucoes[indice_maior]}")
print(f"Melhor Resultado Obtido: {max(resultados)}")
print(f"Média dos Resultados: {np.mean(resultados):.3f}")
print(f"Desvio Padrão dos Resultados: {np.std(resultados):.3f}")
print("\n--------------------------------------------------\n")


# (c) Heurística Gulosa
razoes = v / w
indices_ordenados = np.argsort(razoes)[::-1] # Decrescente

valor_guloso = 0
peso_somatoria = 0
for i in indices_ordenados:
    if peso_somatoria + w[i] <= Capacidade:
        peso_somatoria += w[i]
        valor_guloso += v[i]

print("--------------- Heurística Gulosa ---------------\n")
print(f"Valor Guloso: {valor_guloso}")
print(f"Peso Atual: {peso_somatoria}")
print("\n-----------------------------------------------\n")