# Check Palindrome by Filtering Non-Letters 07.01.2026

- 01/07/2026

- Primeiro pensei em como pegar todas as letras de code e colocar dentro de uma variavel
- Depois disso preciso converter todas para maisculo, se não na hora de comparar ele vai dar erro e não vai entender
- Comparar code com a variavel e retornar true

  result = ''.join(char for char in code.lower() if char.isalpha())

    result = re.sub(r'[^a-zA-Z]','',code)  
Ambos jeitos acima estão certos para resolver isso

A primeira opção é a mesma coisa aqui:
`result = ""

for char in code.lower():
if char.isalpha():
result += char`

    palindrome = result[::-1]

    if result == palindrome:

        return True

    if result != palindrome:

        return False

Utilizamos o método isalpha para verificar se é String ou não, ele retorna como True, caso retornar como True, ele incremente em result
Após isso invertemos a ordem em uma nova variavel(`palindrome`) utilizando [::-1], que é uma técnica de fatiamento (_slicing_) usada para **inverter** sequências (como strings, listas ou tuplas) de forma rápida
Validamos se result é igual palindrome

<hr>
## Lógica

- Primeiro pensei em como pegar apenas as letras da string `code`.
- Depois, converti todas as letras para minúsculas usando `lower()`, pois letras maiúsculas e minúsculas são consideradas diferentes na comparação.
- Em seguida, basta comparar a string original (tratada) com sua versão invertida.
- Se forem iguais, retorna `True`; caso contrário, retorna `False`.

## Maneiras de remover caracteres que não são letras

### 1. Com compreensão de lista (mais comum)

```python
result = ''.join(char for char in code.lower() if char.isalpha())
```

### 2. Com Regex

```python
result = re.sub(r'[^a-zA-Z]', '', code).lower()
```

> **Ambas as abordagens resolvem o problema.**

## Equivalente da primeira opção usando `for`

```python
result = ""

for char in code.lower():
    if char.isalpha():
        result += char
```

A compreensão de lista (`join`) faz exatamente a mesma coisa que esse `for`, porém de forma mais compacta.

## Invertendo a string

```python
palindrome = result[::-1]
```

O fatiamento (`[::-1]`) é uma técnica de **slicing** utilizada para inverter rapidamente uma sequência (string, lista ou tupla).

## Comparação

```python
if result == palindrome:
    return True

return False
```

Também poderia ser simplificado para:

```python
return result == palindrome
```

## Métodos utilizados

### `lower()`

Converte todos os caracteres para minúsculos.

Exemplo:

```python
"ArThUr".lower()
# "arthur"
```

### `isalpha()`

Verifica se um caractere é uma letra do alfabeto.

Retorna:

- `True` → se for uma letra.
- `False` → caso seja número, espaço ou símbolo.

Exemplo:

```python
"a".isalpha()   # True
"8".isalpha()   # False
"!".isalpha()   # False
```

Durante o `for`, sempre que `char.isalpha()` retorna `True`, o caractere é adicionado à variável `result`.

## Complexidade

- **Tempo:** `O(n)`
- **Espaço:** `O(n)`

Percorremos a string uma vez para criar `result` e outra para compará-la com sua versão invertida.
