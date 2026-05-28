#Leitura das entradas
t, n = map(int, input().split())

#Leitura dos valores preditos e ground-truth 
for _ in range(n):
    y_hat, y_true = map(int, input().split())

mse = 0.33
#Exemplo de exibição da parte inteira do MSE
print(int(mse))