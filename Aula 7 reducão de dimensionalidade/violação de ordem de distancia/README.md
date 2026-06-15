# Atividade Violação da Ordem de Distâncias

## Descrição

Construa um programa que receba quatro inteiros `s` (`0 ≤ s ≤ 1024`), `n` (`0 ≤ n ≤ 10³`), `m` (`0 ≤ m ≤ n`) e `c` (`0 ≤ c < m`), indicando uma seed para geração pseudoaleatória de números, o número de amostras, a dimensão dos dados e o número de componentes do PCA, nesta ordem.

A partir dessas entradas, o programa deve calcular o PCA utilizando SVD, conforme visto em aula, e exibir a quantidade de triplas `(i, j, k)` para as quais a seguinte condição não é satisfeita:

```text
1( ||xi − xj||2 < ||xi − xk||2 ) = 1( ||x̂i − x̂j||2 < ||x̂i − x̂k||2 )
```

Para todo `i`, `j`, `k` distintos.

Nessa formulação, `x` e `x̂` correspondem, respectivamente, aos dados no espaço original de dimensão `m` e aos dados projetados nos `k` componentes principais do PCA.

## Observações

Diferentemente dos outros problemas, aqui os dados são gerados de forma pseudoaleatória a partir da seed fornecida, conforme ilustra parte do código abaixo; desta forma, é importante que você não altere esse trecho.

Para o cálculo do SVD, utilize:

```python
np.linalg.svd(., full_matrices=False)
```

Para o cálculo da distância entre duas amostras, use:

```python
np.linalg.norm(., ord=2)
```

Não altere o processo de centralização dos dados nem a ideia geral da contagem já implementada.

## Trecho de código

```python
import numpy as np
import random
from itertools import permutations

np.random.seed(s)
random.seed(s)

X = np.random.randn(n, m)
Xc = X - X.mean(axis=0)

cont = 0
for i, j, k in permutations(range(n), 3):
    xi, xj, xk = X[i], X[j], X[k]

    if ??? != ???:
        cont += 1
```

## Exemplos

As tabelas abaixo apresentam exemplos de entradas e as respectivas saídas do programa. Note que, para obter as saídas esperadas, é preciso executar a geração pseudoaleatória conforme o código acima.

### Exemplo 1

Entrada:

```text
0 15 5 2
```

Saída:

```text
528
```

### Exemplo 2

Entrada:

```text
64 20 12 2
```

Saída:

```text
1506
```
