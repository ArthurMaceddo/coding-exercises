
Esse parecia ser um desafio simples, mas acabou me tomando mais tempo do que eu esperava.

Minha primeira solução foi utilizando **força bruta**, pois foi a abordagem mais direta que consegui pensar. Depois de algumas tentativas, precisei assistir a um vídeo explicando a lógica do problema. Eu até havia olhado a solução oficial do LeetCode, mas não consegui entender a ideia naquele momento. O vídeo foi o que realmente me ajudou a compreender a lógica por trás da solução.

A minha primeira implementação possui complexidade **O(n²)**. Ela não atende ao requisito de eficiência do exercício e não passa em todos os testes do LeetCode, mas acredito que seria suficiente para explicar meu raciocínio em uma entrevista.

---

# Minha primeira solução (Brute Force)

```python
max_profit = 0

for i in range(len(prices)):
    for j in range(i + 1, len(prices)):
        profit = prices[j] - prices[i]

        if profit > max_profit:
            max_profit = profit

return max_profit
```

## Como essa solução funciona?

Utilizamos dois loops:

- `i` representa o dia em que compramos a ação.
    
- `j` representa um possível dia para vendê-la.
    

Para cada combinação possível, calculamos o lucro:

```python
profit = prices[j] - prices[i]
```

Se esse lucro for maior que o maior lucro encontrado até aquele momento (`max_profit`), atualizamos seu valor.

Como `max_profit` começa em `0`, nunca retornaremos um lucro negativo.

### Complexidade

- **Tempo:** `O(n²)` 
    
- **Espaço:** `O(1)` 
    

---

## Vídeo que me ajudou

Esse foi o vídeo que finalmente fez a lógica "clicar" para mim:

[https://www.youtube.com/watch?v=kJZrMGpyWpk](https://www.youtube.com/watch?v=kJZrMGpyWpk)

---

# Solução otimizada

```python
min_price = float('inf')
max_profit = 0

for price in prices:

    if price < min_price:
        min_price = price

    profit = price - min_price

    if profit > max_profit:
        max_profit = profit

return max_profit
```

## Por que usar `float('inf')`?

Inicializamos `min_price` com infinito porque queremos garantir que **o primeiro preço do array sempre será menor**.

Assim, na primeira iteração, `min_price` será atualizado automaticamente.

---

## Como essa solução funciona?

Enquanto percorremos o array apenas uma vez:

1. Verificamos se encontramos um novo menor preço.
    

```python
if price < min_price:
    min_price = price
```

2. Calculamos quanto ganharíamos se vendêssemos a ação no preço atual.
    

```python
profit = price - min_price
```

3. Caso esse lucro seja maior que qualquer outro encontrado anteriormente, atualizamos `max_profit`.
    

```python
if profit > max_profit:
    max_profit = profit
```

---

## Exemplo

Para o array:

```text
[7, 1, 5, 3, 6, 4]
```

A evolução do lucro fica assim:

|Lucro Atual|Maior Lucro|
|--:|--:|
|0|0|
|0|0|
|4|4|
|2|4|
|5|5|
|3|5|

Ao final, retornamos:

```python
5
```

---

# 💡 A principal ideia

A frase mais importante para lembrar desse problema é:

> **Sempre mantenha o menor preço visto até agora.**

Pensando dessa forma, basta responder três perguntas durante cada iteração:

1. **Esse é o menor preço que já encontrei?**
    
    - Sim → atualizo `min_price`.
        
2. **Se eu vendesse hoje, quanto eu lucraria?**
    

```python
profit = price - min_price
```

3. **Esse lucro é maior do que qualquer outro que já encontrei?**
    
    - Sim → atualizo `max_profit`.
        

---

## Complexidade

- **Tempo:** `O(n)` ✅
    
- **Espaço:** `O(1)` ✅
    

Essa abordagem percorre o array apenas uma vez e é a solução esperada pelo LeetCode.