# Atividade: Análise de Matriz de Confusão

Este repositório contém a implementação de um programa para analisar uma **Matriz de Confusão** de dimensões $d \times d$. O objetivo é extrair métricas básicas de desempenho do classificador a partir dos dados da matriz.

## 📝 Enunciado do Problema

Implemente um programa que receba um inteiro $d$ ($1 \le d \le 10^3$), indicando as dimensões de uma matriz de confusão $M \in \mathbb{R}^{d \times d}$.

Em seguida, o programa deve ler os valores da matriz, linha por linha, no formato inteiro. Após ler todos os dados, o programa deve calcular e exibir, na ordem:

1. **(i)** A quantidade total de amostras preditas.
2. **(ii)** A quantidade de amostras preditas corretamente (elementos da diagonal principal).
3. **(iii)** A quantidade de amostras preditas incorretamente (elementos fora da diagonal principal).

### ⚠️ Observação de Formatação

Exiba os pontos **(i)**, **(ii)** e **(iii)** em uma **única linha**, separados apenas por um espaço (não pule linha na saída).

---

## 📊 Exemplos de Entrada e Saída

### Exemplo 1

**Entrada:**

````text
2
3 4
2 1

**Saída:**

```text
10 4 6

````

### Exemplo 2

**Entrada:**

````text
3
1 1 4
1 1 2
3 1 1

**Saída:**

```text
15 3 12

````
