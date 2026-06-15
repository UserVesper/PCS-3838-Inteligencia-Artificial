# Atividade Variância Explicada

Este projeto implementa um programa para calcular a menor quantidade de componentes principais necessárias para atingir uma variância explicada acumulada mínima, utilizando PCA com SVD.

## Descrição do problema

O programa recebe três inteiros:

* `s`: seed para geração pseudoaleatória dos dados;
* `n`: número de amostras;
* `m`: dimensão dos dados.

Em seguida, recebe um número real `v`, onde `0 ≤ v ≤ 1`, representando a proporção mínima de variância explicada acumulada desejada.

A partir desses valores, o programa gera uma matriz de dados pseudoaleatória `X`, centraliza os dados e aplica PCA utilizando SVD. Depois, calcula a variância explicada de cada componente principal e exibe a menor quantidade de componentes necessária para que a variância explicada acumulada seja maior ou igual a `v`.

## Entrada

A entrada é composta por:

```text
s n m
v
```

Onde:

* `s` é um inteiro tal que `0 ≤ s ≤ 1024`;
* `n` é um inteiro tal que `0 ≤ n ≤ 10³`;
* `m` é um inteiro tal que `0 ≤ m ≤ n`;
* `v` é um número real no intervalo `[0, 1]`.

## Saída

A saída deve conter um único inteiro, representando a menor quantidade de componentes principais necessária para atingir a variância explicada acumulada mínima `v`.

## Geração dos dados

Diferentemente de outros exercícios, os dados não são lidos diretamente da entrada. Eles são gerados de forma pseudoaleatória a partir da seed `s`.

O trecho abaixo deve ser mantido sem alterações:

```python
import numpy as np
import random

np.random.seed(s)
random.seed(s)

X = np.random.randn(n, m)
Xc = X - X.mean(axis=0)
```

A matriz `X` contém os dados gerados, e `Xc` representa os dados centralizados pela média de cada coluna.

## PCA utilizando SVD

O PCA deve ser calculado usando decomposição em valores singulares:

```python
U, S, Vt = np.linalg.svd(Xc, full_matrices=False)
```

Para o cálculo da variância explicada, deve-se utilizar apenas os valores de `S²`.

A proporção de variância explicada de cada componente pode ser calculada como:

```python
variancias = S ** 2
proporcoes = variancias / variancias.sum()
```

Depois disso, calcula-se a soma acumulada dessas proporções e encontra-se a menor quantidade de componentes cuja soma seja maior ou igual a `v`.

## Exemplo conceitual

Suponha que `m = 5` e `v = 0.8`.

Se as proporções de variância explicada forem:

```text
0.5, 0.2, 0.15, 0.1, 0.05
```

A soma acumulada será:

```text
0.5
0.7
0.85
```

Como `0.85 ≥ 0.8`, o programa deve exibir:

```text
3
```

Ou seja, são necessários 3 componentes principais.

## Exemplos

### Exemplo 1

Entrada:

```text
0 100 10
0.99
```

Saída:

```text
10
```

### Exemplo 2

Entrada:

```text
64 200 12
0.95
```

Saída:

```text
11
```

## Observações importantes

* A geração dos dados deve seguir exatamente o trecho fornecido no enunciado.
* O processo de centralização dos dados não deve ser alterado.
* A função `np.linalg.svd` deve ser usada com `full_matrices=False`.
* A variância explicada deve ser calculada apenas com base em `S²`.
* A resposta deve ser a menor quantidade de componentes principais necessária para alcançar a variância acumulada `v`.

## Como executar

Salve o código em um arquivo, por exemplo:

```text
main.py
```

Execute com:

```bash
python main.py
```

Depois, insira os dados no formato esperado pela entrada.

## Bibliotecas utilizadas

O programa utiliza as seguintes bibliotecas:

```python
import numpy as np
import random
```

A biblioteca `numpy` é usada para gerar os dados, centralizar a matriz e calcular o SVD.
A biblioteca `random` é usada apenas para manter a seed conforme exigido pelo enunciado.
