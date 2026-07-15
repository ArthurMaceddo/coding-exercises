# Majority Element (LeetCode 169)

This was the first problem I managed to solve after spending a few days without solving anything. 😅

It was definitely a struggle, but I learned a lot throughout the process. My first idea was to use a dictionary (`dict`), but I ended up taking a different approach before coming back to it.

---

# 🚀 My First Solution

```python
n = len(nums) // 2

for num in nums:
    qtty = nums.count(num)
    if qtty > n:
        return num
```

This was the first solution I came up with.

The biggest drawback is its time complexity. Although it works correctly, it repeatedly traverses the array:

* The `for` loop iterates through every element.
* For each element, `count()` scans the entire list again.

As a result, the complexity is:

* **Time:** `O(n²)` ❌
* **Space:** `O(1)` ✅

---

# 📚 Second Solution (Hash Map)

```python
counter = {}
n = len(nums) // 2

for num in nums:

    if num in counter:
        counter[num] = counter[num] + 1
    else:
        counter[num] = 1

    if counter[num] > n:
        return num
```

This approach uses a dictionary to keep track of how many times each number appears.

For every element:

* If it already exists in the dictionary, increment its count.
* Otherwise, initialize its count to `1`.

As soon as any number appears more than `n // 2` times, we can immediately return it.

Complexity:

* **Time:** `O(n)` ✅
* **Space:** `O(n)`

I found this solution harder to come up with, but it's much more efficient than the first one.

---

# ⭐ Best Solution

```python
nums.sort()
return nums[len(nums) // 2]
```

This was the solution that surprised me the most.

At first glance, it almost looks like magic, but there's actually a very simple reason why it works.

## Why does this work?

The problem guarantees that there is a **majority element**, meaning an element that appears **more than half of the time**.

After sorting the array:

* Equal elements become grouped together.
* Since the majority element occupies **more than half of the array**, it **must** include the middle position.

That's why simply returning:

```python
len(nums) // 2
```

always gives the correct answer.

### Example

```text
Before sorting:
[2, 2, 1, 1, 1, 2, 2]

After sorting:
[1, 1, 1, 2, 2, 2, 2]
             ↑
        Middle element
```

Another example:

```text
[3, 3, 4]

Sorted:
[3, 3, 4]
    ↑
```

In both cases, the middle element is guaranteed to be the majority element.

This is probably the easiest solution to understand once you know the reasoning behind it. The hardest part is recognizing this property if you've never seen the problem before.

> **Complexity**
>
> * **Time:** `O(n log n)` (because of sorting)
> * **Space:** Depends on the sorting algorithm used by the language.

---

# 💡 An Even Better Solution

The optimal approach uses the **Boyer-Moore Voting Algorithm**, which solves the problem with:

* **Time:** `O(n)` ✅
* **Space:** `O(1)` ✅

The algorithm works by maintaining a candidate for the majority element and a counter. As it iterates through the array, it cancels out different elements until only the majority candidate remains.

I found this algorithm really interesting and definitely plan to study it in more detail.

## References

* https://www.geeksforgeeks.org/dsa/boyer-moore-algorithm-for-pattern-searching/
* https://www.ime.usp.br/~pf/algoritmos/aulas/strma.html
