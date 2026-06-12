# Atividade: Detecção de Vazamento de Dados (Data Leakage)

Este repositório contém a implementação de um programa para identificar **vazamento de dados** (data leakage) entre os conjuntos de treinamento e teste. O objetivo é verificar se alguma amostra do conjunto de teste foi erroneamente incluída no conjunto de treino.

## 📝 Enunciado do Problema

Construa um programa que receba três inteiros $n_{train}$ ($1 \le n_{train} \le 10^3$), $n_{test}$ ($1 \le n_{test} \le 10^3$) e $m$ ($1 \le m < n_{train}$), indicando o número de amostras de treino, teste e a dimensão dos dados, respectivamente.

Em seguida, o programa deve ler:

1. Um conjunto de dados de treinamento $D_{train} \in \mathbb{R}^{n_{train} \times m}$
2. Um conjunto de teste $D_{test} \in \mathbb{R}^{n_{test} \times m}$

Ambos os conjuntos estão no formato de valores inteiros. Após ler os dados, o programa deve verificar se houve vazamento de dados.

Formalmente, o programa analisa se:
$$D_{train} \cap D_{test} \neq \emptyset$$

- Se houver vazamento de dados (pelo menos uma amostra aparece em ambos os conjuntos), o programa deve exibir o valor **`1`**.
- Caso contrário, deve exibir o valor **`0`**.

---

## 📊 Exemplos de Entrada e Saída

### Exemplo 1 (Sem Vazamento)

**Entrada:**

```text
4 2 3
40 15 72
22 43 82
75 7 34
49 95 75
85 47 63
31 90 20
```

**Saída:**

```text
0

```

### Exemplo 2

**Entrada:**

```text
4 3 4
40 15 72 22
43 82 75 7
34 49 95 75
85 47 63 31
90 20 37 39
34 49 95 75
38 33 58 67


```

**Saída:**

```text
1

```
