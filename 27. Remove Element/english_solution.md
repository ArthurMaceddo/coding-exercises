# Explanation

A simple challenge that uses the **Two Pointers** technique.

The `index` variable represents the position where the next valid element should be placed. Meanwhile, `i` is responsible for iterating through every element in the array.

As `i` traverses the array, every element that is **different** from the target value (`val`) is copied to the position pointed to by `index`. This effectively overwrites the target elements with valid ones, removing all occurrences of the target from the beginning of the array.

## Step by step

- Initialize `index` with `0`. It represents the position where the next non-target element will be stored.
- Iterate through every element in the array using the pointer `i`.
- For each `nums[i]`, check whether it is different from the target value (`val`).
- If `nums[i] != val`, it means the current element should remain in the array.
- Copy the current element to the position indicated by `index`:

```python
nums[index] = nums[i]
```

- Increment `index` by `1` so it points to the next available position for another valid element.
- After the loop finishes, return `index`, since it represents the number of valid elements remaining in the array.

## Code

```python
index = 0

for i in range(len(nums)):
    if nums[i] != val:
        nums[index] = nums[i]
        index += 1

return index
```

<hr>
