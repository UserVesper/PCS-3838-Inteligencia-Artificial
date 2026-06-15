# Atividade: Normalização Min-Max

## Descrição

Similar ao exercício anterior, elabore um programa que receba dois inteiros `n` e `m`, indicando o número de amostras e suas dimensões, respectivamente.

Restrições:

```text id="3h9h6x"
1 ≤ n ≤ 10³
10 ≤ m ≤ 10⁶
```

Em seguida, leia um conjunto de dados `X ∈ Rⁿˣᵐ` no formato inteiro.

Por fim, o programa recebe uma nova amostra `x ∈ R¹ˣᵐ` e deve exibir, apenas a parte inteira, esta amostra normalizada (`x̃`) utilizando a técnica **Min-Max**.

Esta técnica normaliza cada feature `x̃ᵢ` em termos de:

```text
x̃ᵢ = (xᵢ - min(Xᵢ)) / (max(Xᵢ) - min(Xᵢ))
```

onde `min(.)` e `max(.)` indicam o menor e o maior valor de um conjunto, respectivamente.

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
2 0 -3
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
5 0 0 0
```
