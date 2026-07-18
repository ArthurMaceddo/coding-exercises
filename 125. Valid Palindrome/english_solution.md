# My Thought Process

The problem asks us to determine whether a string is a **palindrome**, considering only **letters and numbers** while **ignoring uppercase and lowercase differences**.

To solve this, I first create a cleaned version of the string by:

- Converting all characters to lowercase with `lower()`.
- Keeping only alphanumeric characters using `isalnum()`.
- Joining the filtered characters into a new string.

```python
cleanText = "".join([char for char in s.lower() if char.isalnum()])
```

For example:

```text
Input: "A man, a plan, a canal: Panama"

After cleaning:
"amanaplanacanalpanama"
```

Next, I create a reversed version of the cleaned string using Python slicing.

```python
palindrome = cleanText[::-1]
```

The slice `[::-1]` creates a copy of the string in reverse order.

Finally, I compare the original cleaned string with its reversed version.

```python
return cleanText == palindrome
```

If both strings are identical, the input is a palindrome; otherwise, it is not.

### Time Complexity

- **O(n)** — We traverse the string to clean it and reverse it.

### Space Complexity

- **O(n)** — A new cleaned string and its reversed copy are created.