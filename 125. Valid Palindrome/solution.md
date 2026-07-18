# Meu Raciocínio

O objetivo do problema é verificar se uma string é um **palíndromo**, considerando apenas **letras e números** e **ignorando diferenças entre maiúsculas e minúsculas**.

Para resolver isso, primeiro crio uma nova string contendo apenas os caracteres válidos.

Faço isso da seguinte forma:

- Converto todos os caracteres para minúsculo com `lower()`.
- Utilizo `isalnum()` para manter apenas letras e números.
- Uno todos os caracteres filtrados em uma única string usando `"".join()`.

```python
cleanText = "".join([char for char in s.lower() if char.isalnum()])
```

Por exemplo:

```text
Entrada:
"A man, a plan, a canal: Panama"

Após a limpeza:
"amanaplanacanalpanama"
```

Depois, crio uma versão invertida dessa string utilizando o fatiamento do Python.

```python
palindrome = cleanText[::-1]
```

A sintaxe `[::-1]` retorna uma cópia da string em ordem inversa.

Por fim, basta comparar a string original com sua versão invertida.

```python
return cleanText == palindrome
```

Se ambas forem iguais, significa que a string é um palíndromo. Caso contrário, ela não é.

### Complexidade de Tempo

- **O(n)** — Percorremos a string para limpá-la e também para gerar sua versão invertida.

### Complexidade de Espaço

- **O(n)** — São criadas uma nova string limpa e uma cópia invertida dela.