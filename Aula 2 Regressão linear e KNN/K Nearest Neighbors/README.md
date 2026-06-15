# Atividade Nearest Neighbors

## Descrição

Construa um programa que receba três inteiros `n` (1 ≤ n ≤ 10³), `m` (1 ≤ m ≤ 10⁶) e `k` (1 ≤ k ≤ n), indicando o número de amostras, suas dimensões e o parâmetro `k` do classificador Nearest Neighbors, nesta ordem.

Em seguida, leia um conjunto de dados `X ∈ Rⁿˣᵐ` e seus respectivos rótulos `Y ∈ Rⁿˣ¹`, ambos no formato inteiro.

Como no exercício anterior, os valores que compõem `Y` estão no último índice das `n` entradas fornecidas.

Neste exercício, cada amostra de `Y` indica a categoria da amostra dentre `c` possíveis classes; isto é,

```text
Y ∈ {0, 1, 2, ..., c}
```

Após receber os dados `X` e `Y`, normalize `X` utilizando a técnica **z-score**.

Nesta etapa, considere as estatísticas da população (isto é, `1/n`).

Por fim, o programa recebe uma nova amostra `x ∈ R¹ˣᵐ` e deve exibir a classe predita pelo classificador **Nearest Neighbors** considerando o valor `k` informado.

### Observações

1. Desconsidere casos de empate.
2. Para o cálculo de proximidade, considere a distância euclidiana.
3. Para facilitar a implementação, você pode utilizar `np.linalg.norm(., ord=2)` e `mode` disponíveis nos pacotes `numpy` e `scipy` para o cálculo da distância e moda, respectivamente.

---

## Exemplos

### Exemplo 1

**Entrada**

```text
3 2 1
40 15 3
72 22 0
43 82 2
49 95
```

**Saída**

```text
2
```

---

### Exemplo 2

**Entrada**

```text
4 3 3
40 15 72 2
22 43 82 4
75 7 34 4
49 95 75 4
37 39 67
```

**Saída**

```text
4
```
