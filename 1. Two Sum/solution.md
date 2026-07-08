# Two Sum - Minha Explicação

No começo, achei esse desafio bem complexo. Não consegui resolvê-lo sem antes olhar algumas soluções, mas depois de entender a lógica consegui explicar o funcionamento de cada abordagem.

O objetivo do exercício é encontrar **dois números** dentro de um array cuja soma seja igual ao `target` e retornar **os índices** desses dois elementos.

Existem três formas comuns de resolver esse problema:

- **Brute Force**
    
- **Two-pass Hash Table**
    
- **One-pass Hash Table**
    

---

## Meu primeiro pensamento

Quando comecei a resolver o exercício, a primeira ideia que tive foi comparar cada elemento com todos os próximos elementos do array.

Se a soma não fosse igual ao `target`, eu simplesmente passaria para o próximo índice e repetiria o processo até encontrar a combinação correta.

Ou seja, minha primeira solução seria utilizar **Brute Force**, que é a abordagem mais simples de entender. A ideia é usar **dois `for`**, testando todas as combinações possíveis até encontrar a soma desejada.

---

# Brute Force

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []
```

Essa é a forma mais simples de resolver o problema.

Percorremos todas as combinações possíveis utilizando dois loops e verificamos se a soma dos dois números é igual ao `target`.

O detalhe que eu não percebi quando tentei resolver sozinho foi utilizar `i + 1` no segundo `for`.

Se começássemos em `0` novamente, acabaríamos comparando um elemento com ele mesmo e repetindo comparações que já foram feitas.

Utilizando `i + 1`, garantimos que:

- Não comparamos o mesmo elemento consigo mesmo.
    
- Não repetimos pares já analisados.
    
- Percorremos apenas as combinações necessárias.
    

---

# One-pass Hash Table

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevMap = {}

        for index, item in enumerate(nums):

            diff = target - item

            if diff in prevMap:
                return [prevMap[diff], index]

            prevMap[item] = index

        return []
```

Aqui a lógica muda completamente.

Em vez de testar todas as combinações possíveis, armazenamos os números que já percorremos em um dicionário chamado `prevMap`.

O dicionário possui a estrutura:

```python
valor : índice
```

Por exemplo:

```python
{
    2: 0,
    7: 1,
    11: 2
}
```

A cada número do array fazemos o seguinte:

1. Calculamos quanto falta para atingir o `target`.
    

```python
diff = target - item
```

2. Verificamos se esse valor (`diff`) já existe dentro do `prevMap`.
    

Se existir, significa que já encontramos anteriormente o número que completa a soma.

Então basta retornar os índices:

```python
return [prevMap[diff], index]
```

Caso o valor ainda não exista, armazenamos o número atual no dicionário:

```python
prevMap[item] = index
```

Assim, quando os próximos elementos forem percorridos, eles poderão utilizar esse número para formar a soma desejada.

---

## Conclusão

Na minha opinião, o **Brute Force** é muito mais fácil de entender, principalmente para quem está começando.

Já a solução utilizando **Hash Table** exige um pouco mais de raciocínio, mas é muito mais eficiente, pois percorre o array apenas uma vez e evita testar todas as combinações possíveis.

Depois de entender a ideia do `diff` e do `prevMap`, a lógica passa a fazer bastante sentido e fica bem mais simples visualizar por que essa solução é considerada a melhor para esse problema.

<hr>
