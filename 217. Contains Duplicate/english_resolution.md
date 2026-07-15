# Contains Duplicate (LeetCode 217)

This was a pretty straightforward problem. The goal is simply to determine whether an array contains any duplicate values.

---

# 🚀 My First Solution

```python
lista = list(set(nums))

nums.sort()
lista.sort()

if nums != lista:
    return True
else:
    return False
```

My initial idea was simple:

* Convert the array into a `set`, which automatically removes duplicate values.
* Convert the `set` back into a list.
* Sort both lists, since a `set` does not preserve the original order.
* Compare the two lists. If they are different, then the original array contained duplicates.

Although this solution works, it performs unnecessary operations by creating another list and sorting both lists just to compare them.

### Complexity

* **Time:** `O(n log n)`
* **Space:** `O(n)`

---

# 📚 A Simpler Solution

Later, I came across a similar idea and tried to recreate it on my own. When I checked the official solutions, I realized this was exactly one of the recommended approaches.

```python
return len(nums) != len(set(nums))
```

This solution is both short and elegant.

The reasoning is straightforward:

* `set(nums)` removes all duplicate elements.
* If the size of the `set` is smaller than the original array, then duplicates must exist.

### Example

```text
nums = [1, 2, 3, 1]

len(nums) = 4
len(set(nums)) = 3

4 != 3 → True
```

### Complexity

* **Time:** `O(n)`
* **Space:** `O(n)`

---

# ⭐ Best Approach for Interviews

Although the previous solution is the shortest, interviewers often prefer seeing the duplicate detection implemented explicitly with a `set`.

```python
seen = set()

for num in nums:

    if num in seen:
        return True

    seen.add(num)

return False
```

## Why is this approach preferred?

As we iterate through the array:

* If the current number is already in the `set`, we've found a duplicate and can immediately return `True`.
* Otherwise, we add it to the `set` and continue.

The biggest advantage is that the algorithm can **terminate early** as soon as a duplicate is found, instead of always processing the entire array.

### Example

```text
nums = [1, 2, 3, 2]

seen = {}

1 → add
2 → add
3 → add
2 → already exists → return True
```

### Complexity

* **Time:** `O(n)` (it may finish earlier in the best case)
* **Space:** `O(n)`

---

# 💭 Conclusion

All three solutions solve the problem, but each has different trade-offs.

| Solution                      |     Time     |  Space | Notes                                                                                 |
| ----------------------------- | :----------: | :----: | ------------------------------------------------------------------------------------- |
| Comparing two lists           | `O(n log n)` | `O(n)` | Works, but performs unnecessary sorting and comparisons.                              |
| `len(nums) != len(set(nums))` |    `O(n)`    | `O(n)` | The shortest and most elegant solution.                                               |
| Using a `seen` set            |    `O(n)`    | `O(n)` | Commonly preferred in interviews because it can stop as soon as a duplicate is found. |
