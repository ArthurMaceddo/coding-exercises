# 242. Valid Anagram

## My Thought Process

I was able to solve this problem without too much difficulty.

My first idea was to use a **dictionary (HashMap)** to count how many times each character appears in each string. Before implementing it, I quickly reviewed the Python dictionary documentation to refresh my memory on how to add and update values.

The logic was straightforward:

- If the two strings have different lengths, they can never be anagrams.
- Traverse each string and count the frequency of every character.
- At the end, compare the two dictionaries. If they are identical, both strings contain exactly the same characters with the same frequencies.

### Solution Using Dictionaries

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

This solution runs in **O(n)** time because each string is traversed only once.

---

# Using `Counter`

After solving the problem, I looked at other solutions and discovered Python's `Counter` class from the `collections` module.

`Counter` does exactly what my loops were doing manually: it automatically counts the frequency of elements in an iterable, such as a string or a list.

That makes the solution much shorter:

```python
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return Counter(s) == Counter(t)
```

This solution has the same time complexity as the dictionary approach but is much more concise.

---

# Solution Using Sorting

While solving the exercise, I also thought of another approach.

If two words are anagrams, then after sorting their characters, they should produce exactly the same sequence.

My first implementation was to manually create two lists, append each character, sort them, and compare the results.

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

Later, I realized this could be simplified.

Since `sorted()` can take a string directly and returns a sorted list of its characters, there is no need to build the lists manually.

The entire solution becomes:

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
```

Although this approach is very readable, sorting increases the time complexity.

---

# Comparing the Solutions

| Solution | Time | Space |
|----------|:----:|:-----:|
| Dictionary (HashMap) | **O(n)** | **O(n)** |
| `Counter` | **O(n)** | **O(n)** |
| Sorting (`sorted`) | **O(n log n)** | **O(n)** |

---

# Conclusion

This exercise was a great reminder that the same problem can often be solved in multiple ways.

- The **HashMap** solution is useful for understanding how frequency counting works internally.
- The **`Counter`** solution achieves the same result using a built-in tool from Python's standard library, making the code much cleaner.
- The **sorting** solution is elegant and easy to read, although it has a higher time complexity because of the sorting step.

Overall, this was a great exercise for practicing dictionaries, learning about `Counter`, and comparing different approaches to solving the same problem.