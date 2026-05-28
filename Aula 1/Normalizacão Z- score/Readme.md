# Atividade: Normalização Z-Score

## Descrição

Elabore um programa que receba dois inteiros `n` e `m`, indicando o número de amostras e suas dimensões, respectivamente.

Restrições:

```text
1 ≤ n ≤ 10³
10 ≤ m ≤ 10⁶
```

Em seguida, leia um conjunto de dados `X ∈ Rⁿˣᵐ` no formato inteiro.

Após receber todos os dados de `X`, calcule a média e o desvio padrão de `X` considerando as estatísticas da população, isto é, `1/n`.

Por fim, o programa recebe uma nova amostra `x ∈ R¹ˣᵐ` e deve exibir, apenas a parte inteira, esta amostra normalizada utilizando a técnica **Z-Score**.

---

## Observações

1. Note que o programa realiza a normalização da amostra `x` a partir das estatísticas obtidas com os dados `X`.

2. Na prática, as normalizações não realizam nenhuma das conversões para inteiros que estamos adotando aqui.

---

## Exemplos

As tabelas abaixo apresentam exemplos de entradas e as respectivas saídas do programa.

### Exemplo 1

**Entrada**

```text
2 3
40 15 72
22 43 82
75 7 34
```

**Saída**

```text
4 -1 -8
```

---

### Exemplo 2

**Entrada**

```text
3 4
40 15 72 22
43 82 75 7
34 49 95 75
85 47 63 31
```

**Saída**

```text
12 0 -1 0
```
