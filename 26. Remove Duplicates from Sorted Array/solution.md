# PORTUGUESE  PR-BR
# Explicação

O objetivo deste problema é remover os valores duplicados do array ordenado `nums` **in-place**, mantendo apenas uma ocorrência de cada número.

```python
k = 1

for i in range(1, len(nums)):
    if nums[i] != nums[k - 1]:
        nums[k] = nums[i]
        k += 1

return k
```

## O que representam `i` e `k`?

- **`i`** → Percorre todos os elementos do array (**ponteiro de leitura**).
    
- **`k`** → Indica a posição onde o próximo elemento único será armazenado (**ponteiro de escrita**).
    

## Raciocínio utilizado

Meu primeiro pensamento foi que eu precisava percorrer todos os elementos da lista.

Não podia começar pelo índice `0`, pois o primeiro elemento já é considerado único. Por isso, iniciamos `k` com o valor `1` e começamos o `for` no índice `1`, comparando sempre o elemento atual com o último elemento único armazenado.

A lógica é a seguinte:

- Comparar o elemento atual (`nums[i]`) com o último elemento único salvo (`nums[k - 1]`).
    
- Se eles forem diferentes, significa que encontramos um novo valor único.
    
- Esse valor é copiado para `nums[k]`.
    
- Em seguida, incrementamos `k` para apontar para a próxima posição disponível.
    
- Ao final, retornamos `k`, que representa a quantidade de elementos únicos presentes no array.
    

## Exemplo

```text
nums = [0,0,1,1,1,2,2,3,3,4]

k = 1

i = 1 -> 0 == 0 -> Ignora
i = 2 -> 1 != 0 -> nums[1] = 1, k = 2
i = 3 -> 1 == 1 -> Ignora
i = 4 -> 1 == 1 -> Ignora
i = 5 -> 2 != 1 -> nums[2] = 2, k = 3
...
```

Resultado final:

```text
[0,1,2,3,4,_,_,_,_,_]
```

As primeiras `k` posições do array contêm apenas os elementos únicos, mantendo a ordem original. Os elementos após `k` podem ser ignorados, conforme descrito no enunciado do problema.

## Complexidade

- **Tempo:** `O(n)`, pois percorremos o array apenas uma vez.
    
- **Espaço:** `O(1)`, já que a modificação é feita diretamente no array, sem utilizar estruturas auxiliares.