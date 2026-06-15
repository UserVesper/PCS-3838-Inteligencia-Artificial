# Atividade SVM - Identificar Vetores de Suporte

Este projeto implementa um programa em Python para identificar a quantidade de vetores de suporte em um modelo SVM linear binário.

O programa recebe como entrada os parâmetros de um hiperplano já treinado, representado pelo vetor de pesos `w` e pelo bias `b`, além de um conjunto de dados `X`. A partir desses valores, o programa calcula quais amostras estão sobre as margens do SVM.

## Ideia do exercício

Em um SVM linear, a fronteira de decisão é dada por:

```text
w · x + b = 0
```

As margens do SVM ficam em:

```text
w · x + b = 1
```

e

```text
w · x + b = -1
```

Os pontos que estão sobre essas margens são chamados de **vetores de suporte**.

Portanto, para cada amostra `x`, o programa calcula:

```python
valor = np.dot(w, x) + b
```

Se o valor for próximo de `1` ou `-1`, então essa amostra é considerada um vetor de suporte.

Como estamos trabalhando com números de ponto flutuante, é usada a função `np.isclose`, com tolerância `atol=1e-3`.

## Entrada

A entrada começa com dois inteiros:

```text
n m
```

Onde:

* `n` é a quantidade de amostras;
* `m` é a dimensão de cada amostra.

Depois, o programa lê o vetor `w`, com `m` valores reais:

```text
w1 w2 ... wm
```

Em seguida, lê o bias `b`:

```text
b
```

Por fim, lê a matriz `X`, com `n` linhas e `m` colunas:

```text
x11 x12 ... x1m
x21 x22 ... x2m
...
xn1 xn2 ... xnm
```

## Saída

A saída é um único número inteiro, representando a quantidade de vetores de suporte encontrados.

## Exemplo 1

### Entrada

```text
5 2
-0.9442 -1.4277
6.4345
0.8730 4.7143
2.1993 2.3519
2.8163 1.0193
1.9263 4.1524
2.84382 3.3265
```

### Saída

```text
2
```

## Exemplo 2

### Entrada

```text
6 3
-0.0682 -0.4551 0.0626
0.8990
1.3868 4.4478 3.5095
1.5512 -0.6624 2.1757
1.2313 -0.0328 2.7127
1.9263 4.1524 1.9520
1.7373 4.4254 2.4991
1.2107 -2.3809 0.3648
```

### Saída

```text
3
```

