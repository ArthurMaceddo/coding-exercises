## My Thought Process

At first, I searched for how to check whether an element from one array exists in another. I found an explanation of the brute-force approach, and after understanding it, I implemented it on LeetCode.

The idea is simple: compare every element in `nums1` with every element in `nums2`. If both values are equal and the value is not already present in `newArray`, add it using `append()`.

```python
newArray = []

for i in nums1:
    for j in nums2:
        if i == j and i not in newArray:
            newArray.append(i)

return newArray
```

This solution works, but it has poor performance because it compares every element with every other element.

---

After solving it this way and explaining my reasoning, ChatGPT asked if I remembered Python's `set`. At first I didn't, but then I remembered that a `set` stores only unique values. That led me to a much cleaner solution:

```python
newSet = set(nums1)
newSet2 = set(nums2)

result = list(newSet & newSet2)

return result
```

The `&` operator returns the **intersection** of the two sets, meaning all values that exist in both collections.

---

It can be simplified even further into a single line:

```python
return list(set(nums1) & set(nums2))
```

Both `set` solutions follow the same idea:

1. Convert both lists into sets, automatically removing duplicates.
2. Find the intersection using the `&` operator.
3. Convert the result back into a list, since the problem expects a list as the return value.

This approach is much cleaner, easier to read, and significantly more efficient than the brute-force solution.