# Majority Element (LeetCode 169)

Primeiro problema que consegui resolver depois de alguns dias sem conseguir finalizar nenhum exercício. 😅

Foi um verdadeiro sufoco até chegar na solução. Minha primeira ideia foi utilizar um dicionário (`dict`), mas durante a resolução acabei seguindo outro caminho.

---

# 🚀 Minha primeira solução

```python
n = len(nums) // 2

for num in nums:
    qtty = nums.count(num)
    if qtty > n:
        return num
```

Essa foi a primeira solução que consegui pensar.

O problema dela é a sua complexidade de tempo. Apesar de funcionar corretamente, ela acaba percorrendo o array diversas vezes:

* O `for` percorre todos os elementos.
* Para cada elemento, o método `count()` percorre novamente toda a lista.

Por isso, sua complexidade é:

* **Tempo:** `O(n²)` ❌
* **Espaço:** `O(1)` ✅

---

# 📚 Segunda solução (Hash Map)

```python
counter = {}
n = len(nums) // 2

for num in nums:

    if num in counter:
        counter[num] = counter[num] + 1
    else:
        counter[num] = 1

    if counter[num] > n:
        return num
```

Essa abordagem utiliza um dicionário para armazenar quantas vezes cada número aparece.

Sempre que um número é encontrado:

* Se ele já existe no dicionário, incrementamos sua contagem.
* Caso contrário, iniciamos sua contagem com `1`.

Assim que algum número ultrapassar `n // 2` ocorrências, podemos retorná-lo imediatamente.

Complexidade:

* **Tempo:** `O(n)` ✅
* **Espaço:** `O(n)`

Na minha opinião, essa solução já é bem mais elegante, embora tenha sido um pouco mais difícil de chegar nela sozinho.

---

# ⭐ Melhor solução

```python
nums.sort()
return nums[len(nums) // 2]
```

Essa foi a solução que mais me chamou a atenção.

À primeira vista parece até mágica, mas existe uma explicação muito simples.

## Por que isso funciona?

O enunciado garante que existe um **elemento majoritário**, ou seja, um elemento que aparece **mais da metade das vezes**.

Depois que ordenamos o array:

* Os elementos iguais ficam agrupados.
* Como o elemento majoritário ocupa **mais da metade das posições**, ele obrigatoriamente passa pelo centro do array.

Por isso, basta retornar o elemento da posição:

```python
len(nums) // 2
```

### Exemplo

```text
Antes:
[2, 2, 1, 1, 1, 2, 2]

Depois de ordenar:
[1, 1, 1, 2, 2, 2, 2]
             ↑
          elemento do meio
```

Outro exemplo:

```text
[3, 3, 4]

Ordenado:
[3, 3, 4]
    ↑
```

Em ambos os casos, o elemento da posição central é o elemento majoritário.

Essa solução é extremamente simples de implementar. A parte difícil é justamente perceber essa propriedade quando ainda não se conhece o problema.

> **Complexidade**
>
> * Tempo: `O(n log n)` (por causa da ordenação)
> * Espaço: depende do algoritmo de ordenação utilizado pela linguagem.

---

# 💡 Existe uma solução ainda melhor

A solução considerada ideal utiliza o **Algoritmo de Boyer-Moore Voting**, que resolve o problema em:

* **Tempo:** `O(n)` ✅
* **Espaço:** `O(1)` ✅

Ela funciona mantendo um candidato ao elemento majoritário e um contador, eliminando pares de elementos diferentes até restar apenas o candidato correto.

Foi uma lógica que achei bem interessante e pretendo estudá-la com mais calma.

## Referências

* https://www.geeksforgeeks.org/dsa/boyer-moore-algorithm-for-pattern-searching/
* https://www.ime.usp.br/~pf/algoritmos/aulas/strma.html
