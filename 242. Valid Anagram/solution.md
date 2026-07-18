
Esse foi um exercício que consegui resolver sem grandes dificuldades. Minha primeira ideia foi utilizar um **dicionário (HashMap)** para contar quantas vezes cada caractere aparecia em cada string. Antes de implementar, consultei rapidamente a documentação e alguns exemplos sobre dicionários para relembrar a forma correta de adicionar e atualizar valores.

A lógica foi simples:

- Se as strings possuem tamanhos diferentes, elas nunca poderão ser anagramas.
    
- Percorro cada string contando a frequência de cada caractere.
    
- No final, comparo os dois dicionários. Se forem iguais, significa que ambas possuem exatamente os mesmos caracteres com a mesma quantidade de ocorrências.
    

### Solução utilizando dicionários

```python
myDict = {}
mySecDict = {}

if len(s) != len(t):
    return False

for letter in s:
    if letter in myDict:
        myDict[letter] += 1
    else:
        myDict[letter] = 1

for letter in t:
    if letter in mySecDict:
        mySecDict[letter] += 1
    else:
        mySecDict[letter] = 1

return myDict == mySecDict
```

---

## Utilizando `Counter`

Depois de resolver o problema, fui analisar outras soluções e descobri a classe `Counter`, da biblioteca `collections`.

Ela faz exatamente o que meus for estavam realizando manualmente: conta automaticamente a frequência dos elementos de uma coleção, como listas ou strings.

Isso permite simplificar bastante a solução:

```python
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return Counter(s) == Counter(t)
```

---

## Solução utilizando ordenação

Enquanto resolvia o exercício, também pensei em outra estratégia.

Se duas palavras são anagramas, então, após ordenar seus caracteres, ambas devem produzir exatamente a mesma sequência.

Minha primeira implementação foi criar duas listas, adicionar os caracteres manualmente, ordenar cada uma e compará-las.

```python
list1 = []
list2 = []

for letter in s:
    list1.append(letter)

for letter in t:
    list2.append(letter)

list1.sort()
list2.sort()

return list1 == list2
```

Depois percebi que essa solução ainda poderia ser simplificada.

Como `sorted()` já recebe uma string e retorna uma lista ordenada com seus caracteres, não é necessário criar listas manualmente.

A solução pode ser reduzida para:

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
```

---

# Comparação das soluções

|Solução|Tempo|Espaço|
|---|:-:|:-:|
|Dicionário (HashMap)|**O(n)**|**O(n)**|
|`Counter`|**O(n)**|**O(n)**|
|Ordenação (`sorted`)|**O(n log n)**|**O(n)**|

## Conclusão

Esse exercício foi interessante porque mostrou diferentes formas de resolver o mesmo problema.

- A solução com **HashMap** ajuda a entender como funciona a contagem de frequências manualmente.
    
- A solução com **`Counter`** faz exatamente o mesmo trabalho, porém utilizando uma estrutura já pronta da biblioteca padrão do Python.
    
- A solução utilizando **ordenação** é bastante elegante e simples de ler, embora possua uma complexidade maior devido ao processo de ordenação.
    

Foi um bom exercício para praticar tanto o uso de dicionários quanto conhecer ferramentas da biblioteca padrão que simplificam esse tipo de problema.