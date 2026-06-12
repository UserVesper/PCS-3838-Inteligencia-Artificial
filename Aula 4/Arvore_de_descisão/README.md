# Atividade: Classificador Árvore de Decisão

Este repositório contém a implementação de um classificador de **Árvore de Decisão** para dados bidimensionais, desenvolvido como parte de uma atividade prática. O objetivo é treinar o modelo utilizando um conjunto de dados de treino e, em seguida, predizer os rótulos de um conjunto de teste.

## 📝 Enunciado do Problema

Construa um programa que receba dois inteiros $n_{train}$ ($1 \le n_{train} \le 10^3$) e $n_{test}$ ($1 \le n_{test} \le 10^3$), indicando o número de amostras de treino e teste, respectivamente.

Em seguida, o programa deve ler:

1. Um conjunto de dados de treinamento $D_{train} \in \mathbb{R}^{n_{train} \times 2}$
2. Seus respectivos rótulos $Y_{train} \in \{0, 1\}$ (armazenados no último índice de cada linha de treino)
3. Um conjunto de teste $D_{test} \in \mathbb{R}^{n_{test} \times 2}$

Após a leitura, o modelo deve ser treinado utilizando apenas os dados de $D_{train}$ completando a implementação da classe `DecisionTree`. Por fim, o programa deve exibir a classificação dos dados de teste $D_{test}$, separando cada valor por um espaço.

### ⚠️ Observações Importantes

- **Não** realize nenhum tipo de normalização nos dados de entrada.
- Na classe `DecisionTree`, complete e implemente **apenas** o que for solicitado nos trechos indicados por comentários com a marcação `***Implemente***`.
- **Não** faça nenhum tipo de arredondamento nos dados.
- **Não** altere a função `main` (responsável pela leitura dos dados).

---

## 📊 Exemplos de Entrada e Saída

### Exemplo 1

**Entrada:**

```text
6 4
-1.13 0.12 0
-0.11 0.32 1
0.32 -0.31 1
1.16 -0.80 1
0.48 0.19 0
1.86 0.07 1
-0.20 0.79
0.59 0.60
-0.09 0.85
1.76 -0.01


```

**Saída:**

```text
1 1 1 1

```

### Exemplo 2

**Entrada:**

```text
8 4
0.34 0.94 0
1.00 -0.09 0
1.32 -0.48 1
-0.08 0.27 1
-0.96 -0.15 0
1.89 0.88 1
0.58 -0.47 1
1.04 0.57 0
-0.08 1.03
0.35 -0.31
1.89 -0.27
-1.21 0.81

```

**Saída:**

```text
1 0 1 0

```
