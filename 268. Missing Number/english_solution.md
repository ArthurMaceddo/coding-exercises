# Missing Number (LeetCode 268)

My first idea was to sort the array. Once the numbers were in ascending order, I thought it would be much easier to identify where the sequence was broken.

From there, my idea was to compare each element with the next one. If the sequence was correct, the next value should always be **the current value + 1**. If that wasn't the case, then the missing number would simply be **the current value + 1**.

### Example

```text
[0, 1, 3]
```

Comparing the elements:

* `0` → next is `1` ✅
* `1` → next should be `2`, but it's `3` ❌

Therefore, the missing number is **2**.

---

## What I did wrong

The idea itself was correct, but my first implementation was more complicated than necessary.

Initially, I tried solving it using **two nested `for` loops** and comparing different positions in the array.

After thinking about it a little more, I realized there was a much simpler observation.

Once the array is sorted:

> Every position should contain the same value as its index.

In other words:

```text
Index :  0  1  2  3
Array : [0, 1, 2, 3]
```

As soon as this property is no longer true, we've found the missing number.

---

# Solution

```python
nums.sort()

for i in range(len(nums)):
    if nums[i] != i:
        return i

return len(nums)
```

---

## How does this solution work?

First, we sort the array.

Then we iterate through every index and check whether:

```python
nums[i] == i
```

As long as this condition is true, no numbers are missing up to that point.

The first time we find:

```python
nums[i] != i
```

we immediately know that `i` is the missing number.

---

## Example 1

```text
nums = [3, 0, 1]
```

After sorting:

```text
[0, 1, 3]
```

Comparing each index:

| Index | Value |
| ----: | ----: |
|     0 |   0 ✅ |
|     1 |   1 ✅ |
|     2 |   3 ❌ |

Since `nums[2] != 2`, we return:

```python
2
```

---

## Example 2

```text
nums = [0, 1, 2]
```

Every index matches its value.

That means the missing number comes after the last element:

```python
return len(nums)
```

Result:

```text
3
```

---

## Complexity

* **Time:** `O(n log n)` (because of sorting)
* **Space:** `O(1)` (ignoring the sorting algorithm's extra space)

Although there's an optimal **O(n)** solution using either the sum formula or the XOR operation, I found this approach much more intuitive and easier to understand when solving the problem for the first time.
