import numpy as np
import random
from itertools import permutations

#Leitura das entradas
s, n, m, c = map(int, input().split())

np.random.seed(s)
random.seed(s)

X = np.random.randn(n, m)
Xc = X - X.mean(axis=0)

#SVD
U, S, Vt = np.linalg.svd(Xc, full_matrices=False)

componentes = Vt[:c]

X_proj = Xc @ componentes.T

count = 0

#distância entre os pontos no espaço original e no espaço projetado
for i, j, k in permutations(range(n), 3):
    xi, xj, xk = X[i], X[j], X[k]
    xpi, xpj, xpk = X_proj[i], X_proj[j], X_proj[k]

    original = np.linalg.norm(xi - xj, ord=2) < np.linalg.norm(xi - xk, ord=2)

    projetado = np.linalg.norm(xpi - xpj, ord=2) < np.linalg.norm(xpi - xpk, ord=2)

    if original != projetado:
        count += 1

print(count)