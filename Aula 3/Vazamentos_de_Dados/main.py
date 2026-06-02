import numpy as np
#Leitura das entradas
n_train, n_test, m = map(int, input().split())

D_train = np.zeros((n_train, m), dtype=int)

for i in range(n_train):
    D_train[i] = np.array(list(map(int, input().split())))

D_test = np.zeros((n_test, m), dtype=int)

for i in range(n_test):
    D_test[i] = np.array(list(map(int, input().split())))
    
#verificar vazamento

vaza = False

for i in range(n_test):
    for j in range(n_train):
        if np.array_equal(D_test[i], D_train[j]):
            vaza = True
            break

    if vaza:
        break
    
if vaza:
    print('1')
else:
    print('0')