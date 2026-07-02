# Check for Non-Identical String Rotation

## Explicação

Este exercício consiste em verificar se uma string `s2` é uma **rotação** de outra string `s1`, com a condição de que ambas **não sejam idênticas**.

Uma rotação ocorre quando apenas o ponto de início da leitura da string é alterado, mantendo a ordem relativa de todos os caracteres. Por exemplo, a string `abcde` pode ser rotacionada para `bcdea`, `cdeab`, `deabc` ou `eabcd`. Em todos esses casos, a sequência das letras permanece a mesma.

A principal observação para resolver o problema é que, ao concatenar uma string com ela mesma (`s1 + s1`), todas as possíveis rotações de `s1` passam a existir como substrings dessa nova string.

Por exemplo:

```text
s1 = "abcde"

s1 + s1

abcdeabcde
```

Dentro de `abcdeabcde` é possível encontrar todas as rotações de `abcde`:

```text
abcde
bcdea
cdeab
deabc
eabcd
```

Com isso, basta verificar se `s2` está contida em `s1 + s1`. Para realizar essa busca, pode ser utilizado o método `find()`, que retorna o índice onde a substring foi encontrada. Caso ela não exista, o método retorna `-1`.

Antes dessa verificação, ainda é necessário validar duas condições:

- As duas strings devem possuir o mesmo tamanho, caso contrário não podem ser rotações uma da outra.
- As strings não podem ser exatamente iguais, pois o exercício solicita apenas rotações **não triviais**.

Se todas as validações forem satisfeitas e `s2` for encontrada dentro de `s1 + s1`, então a resposta é `1`; caso contrário, a resposta é `0`.

## Complexidade

- **Tempo:** `O(n)`
- **Espaço:** `O(n)`, devido à criação da string concatenada.

<hr>

# Como cheguei na solução (Meu raciocínio)

- O ponto em que fiquei com mais dificuldade foi entender que era uma **rotação**, e não um **anagrama**. Como é uma rotação, existem poucas formas de rotacionar a palavra, e quando eu rotaciono a palavra eu só mudo o ponto em que ela começa.
- Sabendo dessa informação, contatenamos a palavra com ela mesma **palavra + palavra = novaPalavra**.
- Após isso, verifiquei que conseguimos utilizar o método `find()`, que retorna a posição em que começa a string que estamos procurando. Caso ele não encontre, ele retorna `-1`.
- Nós não precisamos saber qual é a posição em que começa a nova palavra, apenas queremos saber se essa verificação não é falsa, pois, se ele conseguir retornar uma posição, significa que `s2` é uma rotação de `s1`.
- Após sabermos isso, basta validar com um `if` se o resultado é diferente de `-1`. Caso seja, retornamos `1`, como solicitado pelo exercício.

Fontes:

https://www.w3schools.com/python/ref_string_find.asp - Explica o método find()
https://www.geeksforgeeks.org/python/python-string-find/ - Explica o método find()
