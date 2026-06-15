import numpy as np

#Leitura da dimensão dos dados
n, m = map(int, input().split())

w = np.array(list(map(float, input().split())))
b = float(input())

X = np.zeros((n, m), dtype=float)
for i in range(n):
    X[i] = np.array(list(map(float, input().split())))

for x in X:
    resultado = w @ x + b
    
    if resultado > 0:
        print(1)
    else:
        print(0)