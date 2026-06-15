# Atividade SVM - Classificação de Dados

## Descrição

Elabore um programa que receba dois inteiros `n` (`1 ≤ n ≤ 10³`) e `m` (`1 ≤ m < n`), indicando a quantidade e dimensão dos dados e, consequentemente, a dimensão da matriz de projeção — hiperplano — do SVM, `w`.

Em seguida, leia o hiperplano `w` e o bias `b` de um modelo SVM binário aprendido. Ambos `w` e `b` são valores em ponto flutuante e separados por uma quebra de linha.

Em seguida, leia um conjunto de dados `X ∈ Rⁿˣᵐ` também como ponto flutuante.

Após realizar a leitura dos dados acima, a partir dos valores de `w` e `b`, o programa deve exibir a classificação realizada pelo SVM, conforme visto em aula.

## Observação

Separe cada classificação pulando uma linha.

## Entrada

A entrada contém:

```text id="aq6smp"
n m
w
b
X
```

Onde:

* `n` é a quantidade de dados;
* `m` é a dimensão dos dados;
* `w` é o hiperplano do modelo SVM;
* `b` é o bias do modelo SVM;
* `X` é o conjunto de dados.

## Saída

A saída deve conter a classificação realizada pelo SVM para cada amostra.

Cada classificação deve ser separada pulando uma linha.

## Exemplos

As tabelas abaixo apresentam exemplos de entradas e as respectivas saídas do programa.

### Exemplo 1

Entrada:

```text id="muoxm2"
5 2
-0.9442 -1.4277
6.4345
0.8730 4.7143
2.1993 2.3519
2.8163 1.0193
1.9263 4.1524
2.84382 3.3265
```

Saída:

```text id="xnz4zy"
0
1
1
0
0
```

### Exemplo 2

Entrada:

```text id="f54295"
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

Saída:

```text id="uoytyf"
0
1
0
0
1
1
```
