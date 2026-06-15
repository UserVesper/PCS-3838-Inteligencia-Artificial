import numpy as np
import random

#Leitura das entradas
s, n, m = map(int, input().split())
v = float(input())

#Não altere
np.random.seed(s)
random.seed(s)

X = np.random.randn(n, m)
Xc = X - X.mean(axis=0)

U, S, Vt = np.linalg.svd(Xc, full_matrices=False)

# Variância  Sigma²
variancias = S ** 2

proporcoes = variancias / np.sum(variancias)

acumulada = np.cumsum(proporcoes)

indices = np.where(acumulada >= v)[0]

# Como queremos a menor quantidade, pegamos o primeiro índice e somamos 1
qtd_componentes = indices[0] + 1

print(qtd_componentes)