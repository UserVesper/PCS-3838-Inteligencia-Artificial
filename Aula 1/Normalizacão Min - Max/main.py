import numpy as np

#Leitura da dimensão dos dados
n, m = map(int, input().split())

#Leitura dos dados X
X = np.zeros((n, m), dtype=int)
for i in range(n):
    X[i] = np.array(list(map(int, input().split())))
    
#Leitura da amostra x
x = np.array(list(map(int, input().split())))

#Implemente aqui a normalização antes de exibir a amostra

for x_i in x.flatten():
    print(int(x_i), end=' ')