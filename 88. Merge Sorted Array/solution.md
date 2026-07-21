```python
nums1[:] = sorted(nums1[:m] + nums2[:n])
```

Minha primeira ideia foi resolver o exercício dessa forma.

Tive que pesquisar como limitar uma lista até uma determinada posição e descobri que isso pode ser feito utilizando `[:m]`, que pega apenas os `m` primeiros elementos da lista.

Depois disso surgiu outro problema. Eu não sabia como modificar a lista original em vez de fazer `nums1` apontar para uma nova lista. Pesquisando, descobri que utilizando `nums1[:]` eu substituo todo o conteúdo da lista original, que é exatamente o que o LeetCode espera.

Apesar de essa solução funcionar e ser aceita, ela não é a forma mais eficiente de resolver o exercício, pois utiliza `sorted()`. A solução esperada utiliza a técnica de **Two Pointers**, alcançando uma complexidade melhor.

# Solução correta

Neste exercício utilizamos três ponteiros:

- `i`: aponta para o último elemento válido de `nums1`.
    
- `j`: aponta para o último elemento de `nums2`.
    
- `k`: aponta para a última posição disponível em `nums1`, onde será colocado o maior elemento da comparação.
    

O principal insight deste exercício é percorrer os arrays **de trás para frente**. Fazendo isso, utilizamos justamente os espaços vazios existentes no final de `nums1`, evitando sobrescrever elementos que ainda precisam ser comparados. Se fizéssemos o processo do início para o fim, correríamos o risco de perder valores importantes de `nums1` antes mesmo de utilizá-los.

Começamos o `while` verificando apenas `j >= 0`, pois nosso objetivo é copiar todos os elementos de `nums2` para `nums1`. Se `nums2` acabar primeiro, os elementos restantes de `nums1` já estarão na posição correta.

Dentro do loop, verificamos se `i < 0` ou se o último elemento de `nums2` é maior que o último elemento válido de `nums1`.

Se isso acontecer, significa que o maior valor disponível está em `nums2`. Então copiamos esse valor para `nums1[k]` e decrementamos `j`, pois esse elemento já foi utilizado e agora devemos comparar o próximo.

Caso contrário, o maior valor está em `nums1`. Nesse caso, copiamos `nums1[i]` para `nums1[k]` e decrementamos `i`, pois esse elemento também já foi utilizado.

Ao final de cada iteração, decrementamos `k`, já que a posição atual foi preenchida corretamente e podemos passar para a próxima posição livre.

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if i < 0 or nums2[j] > nums1[i]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1

            k -= 1
```

## Complexidade

- 🟢 **Tempo:** `O(m + n)`
    
- 🟢 **Espaço:** `O(1)`