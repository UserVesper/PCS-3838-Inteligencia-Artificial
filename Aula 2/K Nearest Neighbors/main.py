import numpy as np
from scipy.stats import mode
# Ler os dados X e suas classes Y
# Normalizar X com Z-Score
# Ler a nova amostra x
# Normalizar x usando a média e o desvio padrão de X
# Calcular a distância entre x e todas as amostras de X
# Ordenar as distâncias
# Pegar os k vizinhos mais próximos
# Escolher a classe mais frequente entre eles

# Leitura das entradas
n, m, k = map(int, input().split())

X = np.zeros((n, m), dtype=int)
Y = np.zeros(n, dtype=int)

# Leitura dos dados X e Y
for i in range(n):
    tmp = np.array(list(map(int, input().split())))
    X[i] = tmp[:-1]  # Valores de X
    Y[i] = tmp[-1]   # Valor de Y


x = np.array(list(map(int, input().split())))

# Normalização Z-Score de X
media_X = np.mean(X, axis=0)
desvio_X = np.std(X, axis=0)

X_norm = (X - media_X) / desvio_X


x_norm = (x - media_X) / desvio_X


distancias = np.zeros(n)

for i in range(n):
    distancias[i] = np.linalg.norm(X_norm[i] - x_norm, ord=2)

# Índices dos k vizinhos mais próximos
indices_vizinhos = np.argsort(distancias)[:k]


rotulos_vizinhos = Y[indices_vizinhos]

# Classe predita
y_hat = mode(rotulos_vizinhos, keepdims=True).mode[0]

print(y_hat)