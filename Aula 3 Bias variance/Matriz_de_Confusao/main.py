import numpy as np

#Leitura da dimensão da matriz (quadrada)
d = int(input())

cm = np.zeros((d, d), dtype=int)

#Leitura da matriz (dxd)
for i in range(d):
    cm[i] = np.array(list(map(int, input().split())))

total = np.sum(cm)
correto = np.trace(cm)
errado = total - correto

print(total, correto, errado)