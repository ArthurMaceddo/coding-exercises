
# Explicação

Um desafio simples que utiliza a técnica de **Two Pointers**.

A variável `index` representa a posição onde o próximo elemento válido deve ser armazenado. Já o ponteiro `i` é responsável por percorrer todos os elementos do array.

Enquanto `i` percorre o array, todo elemento que é **diferente** do valor alvo (`val`) é copiado para a posição indicada por `index`. Dessa forma, os elementos alvo são sobrescritos pelos elementos válidos, removendo todas as ocorrências do valor desejado no início do array.

## Passo a passo

- Inicialize `index` com `0`. Ele representa a posição onde o próximo elemento que não é o alvo será armazenado.
- Percorra todos os elementos do array utilizando o ponteiro `i`.
- Para cada `nums[i]`, verifique se ele é diferente do valor alvo (`val`).
- Se `nums[i] != val`, significa que esse elemento deve permanecer no array.
- Copie esse elemento para a posição indicada por `index`:

```python
nums[index] = nums[i]
```

- Incremente `index` em `1` para apontar para a próxima posição disponível onde outro elemento válido será armazenado.
- Ao final da iteração, retorne `index`, pois ele representa a quantidade de elementos válidos restantes no array.

## Código

```python
index = 0

for i in range(len(nums)):
    if nums[i] != val:
        nums[index] = nums[i]
        index += 1

return index
```