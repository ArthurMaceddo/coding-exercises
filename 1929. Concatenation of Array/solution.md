# Explicação

Este é um desafio simples, sem um nível de dificuldade elevado. Com um conhecimento básico sobre **arrays (listas)** já é possível resolvê-lo, e existem várias maneiras de chegar ao mesmo resultado.

## 1ª Forma

A maneira mais simples é utilizar a multiplicação da lista:

```python
return nums * 2
```

O operador `*` duplica a lista inteira, retornando todos os elementos duas vezes na mesma ordem.

---

## 2ª Forma

Esta abordagem segue exatamente o que o enunciado pede: criar um novo array e adicionar os elementos duas vezes.

```python
ans = []

for n in nums:
    ans.append(n)

for n in nums:
    ans.append(n)

return ans
```

---

## 3ª Forma

Foi a solução que utilizei.

```python
copia = nums.copy()
nums.extend(copia)

return nums
```

Primeiro é criada uma cópia da lista utilizando `copy()`. Em seguida, `extend()` adiciona todos os elementos dessa cópia ao final da lista original.

---

# 💭 Meu raciocínio

Quando li o exercício, já imaginei que seria necessário copiar a lista e adicioná-la novamente ao final dela para obter o resultado esperado.

Depois de finalizar a solução, descobri que também era possível resolver de uma forma muito mais simples utilizando:

```python
nums * 2
```
