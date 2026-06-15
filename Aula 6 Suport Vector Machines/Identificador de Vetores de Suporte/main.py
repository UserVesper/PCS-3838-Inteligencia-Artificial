import numpy as np

#Leitura da dimensão dos dados
n, m = map(int, input().split())

w = np.array(list(map(float, input().split())))
b = float(input())

X = np.zeros((n, m), dtype=float)
for i in range(n):
    X[i] = np.array(list(map(float, input().split())))

count = 0
for x in X:

    valor = np.dot(w,x) + b
    #Utilize a função abaixo para evitar problemas de precisão
    if np.isclose(abs(valor), 1.0, atol=1e-3):
        count += 1

print(count)