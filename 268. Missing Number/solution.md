
Minha primeira ideia foi ordenar o array. Assim, os números ficariam em ordem crescente e seria mais fácil identificar onde existia uma quebra na sequência.

A partir disso, pensei em comparar cada elemento com o próximo. Se a sequência estivesse correta, o próximo valor deveria ser exatamente **o valor atual + 1**. Caso isso não acontecesse, significaria que o número ausente seria justamente **o valor atual + 1**.

### Exemplo

```text
[0, 1, 3]
```

Ao comparar os elementos:

- `0` → próximo é `1` ✅
    
- `1` → o próximo deveria ser `2`, mas é `3` ❌
    

Logo, o número ausente é **2**.

---

## O que eu fiz de errado

O raciocínio estava correto, mas minha primeira implementação acabou ficando mais complicada do que precisava.

Inicialmente, tentei resolver utilizando **dois laços (`for`)** e comparando diferentes posições do array. Depois percebi que isso era desnecessário.

Ao ordenar o array, existe uma propriedade muito interessante:

> Cada posição do array deveria conter exatamente o mesmo valor do seu índice.

Ou seja:

```text
Índice:  0  1  2  3
Array : [0, 1, 2, 3]
```

Se em algum momento essa igualdade deixar de acontecer, significa que encontramos o número que está faltando.

---

# Solução

```python
nums.sort()

for i in range(len(nums)):
    if nums[i] != i:
        return i

return len(nums)
```

---

## Como essa solução funciona?

Primeiro ordenamos o array.

Depois percorremos todos os índices e verificamos se:

```python
nums[i] == i
```

Enquanto essa condição for verdadeira, significa que nenhum número está faltando até aquele ponto.

Quando encontramos o primeiro índice em que:

```python
nums[i] != i
```

podemos retornar `i`, pois esse é exatamente o número ausente.

---

## Exemplo 1

```text
nums = [3, 0, 1]
```

Depois da ordenação:

```text
[0, 1, 3]
```

Comparando:

|Índice|Valor|
|--:|--:|
|0|0 ✅|
|1|1 ✅|
|2|3 ❌|

Como `nums[2] != 2`, retornamos:

```python
2
```

---

## Exemplo 2

```text
nums = [0, 1, 2]
```

Todos os índices correspondem aos seus valores.

Nesse caso, o número ausente é o próximo após o último elemento:

```python
return len(nums)
```

Resultado:

```text
3
```

---

## Complexidade

- **Tempo:** `O(n log n)` (por causa da ordenação)
    
- **Espaço:** `O(1)` (desconsiderando o algoritmo de ordenação)
    

Embora exista uma solução em **O(n)** utilizando a soma dos números ou o operador XOR, achei essa abordagem muito intuitiva e fácil de entender quando estava resolvendo o problema pela primeira vez.