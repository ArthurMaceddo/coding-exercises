# Check Palindrome by Filtering Non-Letters 07.01.2026

**01/07/2026**

## Logic

- First, I needed to extract only the alphabetic characters from the string `code`.
- Then, I converted all letters to lowercase using `lower()`, since uppercase and lowercase letters would otherwise be treated as different characters during comparison.
- Finally, I compared the processed string with its reversed version.
- If both strings are equal, the function returns `True`; otherwise, it returns `False`.

## Ways to remove non-letter characters

### 1. Using a generator expression (most common)

```python
result = ''.join(char for char in code.lower() if char.isalpha())
```

### 2. Using Regular Expressions (Regex)

```python
result = re.sub(r'[^a-zA-Z]', '', code).lower()
```

> **Both approaches correctly solve the problem.**

## Equivalent implementation using a `for` loop

```python
result = ""

for char in code.lower():
    if char.isalpha():
        result += char
```

The generator expression used with `join()` performs the same task as this `for` loop, but in a more concise and Pythonic way.

## Reversing the string

```python
palindrome = result[::-1]
```

The slicing syntax (`[::-1]`) is a common Python technique used to reverse sequences such as strings, lists, and tuples.

## Comparison

```python
if result == palindrome:
    return True

return False
```

This can also be simplified to:

```python
return result == palindrome
```

## Methods used

### `lower()`

Converts all characters in the string to lowercase.

Example:

```python
"ArThUr".lower()
# "arthur"
```

### `isalpha()`

Checks whether a character is an alphabetic letter.

Returns:

- `True` → if the character is a letter.
- `False` → if it is a number, whitespace, or symbol.

Example:

```python
"a".isalpha()   # True
"8".isalpha()   # False
"!".isalpha()   # False
```

During the iteration, whenever `char.isalpha()` returns `True`, the character is appended to the `result` string.

## Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

The algorithm traverses the string once to build `result` and once more to compare it with its reversed version.
