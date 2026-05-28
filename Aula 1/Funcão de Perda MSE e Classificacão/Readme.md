# Atividade: Função de Perda MSE e Classificação

## Descrição

Construa um programa que receba dois inteiros `t` e `n`.

* `t ∈ {0,1}` indica o tipo da tarefa:

  * `t = 0` → regressão
  * `t = 1` → classificação

* `n` indica o número de amostras preditas pelo modelo.

Restrição:

```text id="nclwz0"
1 ≤ n ≤ 10⁶
```

Em seguida, leia `n` pares de valores inteiros representando:

* o valor predito pelo modelo (`ŷ`, com `0 ≤ ŷ ≤ 100`)
* o valor verdadeiro (`y`, com `0 ≤ y ≤ 100`)

de cada amostra.

Ao final:

* No caso de **regressão**, o programa deve exibir, apenas a parte inteira, o valor da função de perda **Mean Squared Error (MSE)** vista em aula.

* No caso de **classificação**, o programa deve exibir a quantidade de amostras classificadas corretamente.

---

## Exemplos

As tabelas abaixo apresentam exemplos de entradas e as respectivas saídas do programa.

### Exemplo 1 — Regressão

**Entrada**

```text id="e3ux9x"
0 3
40 15
72 22
43 82
```

**Saída**

```text id="8d72kz"
1548
```

---

### Exemplo 2 — Classificação

**Entrada**

```text id="f1q2wl"
1 3
0 0
1 3
3 1
```

**Saída**

```text id="ww65zq"
1
```
