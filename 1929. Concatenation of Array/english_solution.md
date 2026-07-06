# Explanation

This is a simple challenge with no real level of difficulty. Having a basic understanding of **arrays (lists)** is enough to solve it, and there are several different ways to reach the same result.

## Solution 1

The simplest approach is to multiply the list:

```python
return nums * 2
```

The `*` operator duplicates the entire list, returning all elements twice while preserving their original order.

---

## Solution 2

This approach follows exactly what the problem statement asks for: create a new array and append all elements twice.

```python
ans = []

for n in nums:
    ans.append(n)

for n in nums:
    ans.append(n)

return ans
```

---

## Solution 3

This is the approach I used.

```python
copy = nums.copy()
nums.extend(copy)

return nums
```

First, a copy of the list is created using `copy()`. Then, `extend()` appends every element from the copied list to the end of the original list.

---

# 💭 My Thought Process

When I first read the problem, I immediately thought that I needed to create a copy of the list and append it to the original one to produce the expected output.

After solving it, I realized there was an even simpler solution:

```python
nums * 2
```
