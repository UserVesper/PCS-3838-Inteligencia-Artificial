import numpy as np
from scipy import linalg

n, m = map(int, input().split())

X = np.zeros((n, m), dtype=int)
Y = np.zeros((n, 1), dtype=int)

for i in range(n):
    tmp = np.array(list(map(int, input().split())))
    X[i] = tmp[:-1]
    Y[i] = tmp[-1]

# Leitura
x = np.array(list(map(int, input().split())))

# normalização Z-Score de X
media_X = np.mean(X, axis=0)
desvio_X = np.std(X, axis=0)

X_norm = (X - media_X) / desvio_X
x_norm = (x - media_X) / desvio_X

# Normalização Z-Score de Y
media_Y = np.mean(Y, axis=0)
desvio_Y = np.std(Y, axis=0)

Y_norm = (Y - media_Y) / desvio_Y

# Aprendizado OLS sem bias
# w = pinv(X) * Y
w = linalg.pinv(X_norm) @ Y_norm

# Predição na escala normalizada
y_hat_norm = x_norm @ w

# Desnormalização para a escala original de Y
y_hat = y_hat_norm * desvio_Y + media_Y

print(int(y_hat[0]))