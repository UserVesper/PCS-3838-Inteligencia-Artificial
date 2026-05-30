# Atividade Ordinary Least Squares (OLS)

## Descrição

Elabore um programa que receba dois inteiros `n` (1 ≤ n ≤ 10³) e `m` (1 ≤ m ≤ n), indicando o número de amostras e suas dimensões, respectivamente.

Em seguida, leia um conjunto de dados `X ∈ Rⁿˣᵐ` e seus respectivos rótulos `Y ∈ Rⁿˣ¹`, ambos no formato inteiro.

Note que os valores que compõem `Y` estão no último índice das `n` entradas fornecidas.

Após receber os dados `X` e `Y`, normalize ambos utilizando a técnica **z-score** e aprenda um modelo **Ordinary Least Squares (OLS)**, conforme visto em aula (slide 10 – Aula 2).

Na etapa de normalização, considere as estatísticas da população (isto é, `1/n`).

Por fim, o programa recebe uma nova amostra `x ∈ R¹ˣᵐ` e deve exibir (apenas a parte inteira – implementação já disponível no código) o valor predito pelo OLS aprendido.

Importantemente, o valor predito deve seguir a escala do `Y` original (antes da normalização); para isso você deve “desnormalizar” o valor predito.

### Observações

1. Desconsidere o termo de bias.
2. Para o cálculo da pseudo-inversa de `X`, empregue a função `linalg.pinv` disponível no pacote `scipy`.

---

## Exemplos

### Exemplo 1

**Entrada**

```text
3 4
40 15 72 22 5
43 82 75 7 10
34 49 95 75 4
37 39 67 4
```

**Saída**

```text
6
```

---

### Exemplo 2

**Entrada**

```text
4 6
40 15 72 22 43 82 7
75 7 34 49 95 75 6
85 47 63 31 90 20 10
37 39 67 4 42 51 1
58 67 69 88 68 46
```

**Saída**

```text
16
```
