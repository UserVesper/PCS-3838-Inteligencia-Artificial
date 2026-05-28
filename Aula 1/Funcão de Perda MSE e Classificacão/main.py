# Leitura das entradas
t, n = map(int, input().split())

mse = 0
acertos = 0


for _ in range(n):
    y_hat, y_true = map(int, input().split())

    #regressão
    if t == 0:
        mse += (y_hat - y_true) ** 2

    # classificação
    else:
        if y_hat == y_true:
            acertos += 1

# Saída
if t == 0:
    mse = mse / n
    print(int(mse))
else:
    print(acertos)