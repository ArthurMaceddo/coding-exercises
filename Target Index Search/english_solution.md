# Binary Search

The first thing we need to understand is what a binary search is. It is an efficient algorithm used to find a specific item in a sorted list of data.

## What is Binary Search?

It starts by looking exactly at the middle of the list. If the middle element is the number we are looking for, the search ends immediately.

If the middle number is smaller than the target, it understands that the target can only be in the right half of the list.

If the middle number is greater than the target, it understands that the target can only be in the left half of the list.

It keeps repeating this process until it finds the target or until there are no elements left to search.

## My Thought Process

When I first read the exercise, I understood that the middle index should be calculated using:

```python
mid = (low + high) // 2
```

because this always finds the middle element of the current search range.

After that, I needed to compare `nums[mid]` with the `target` to know if the value was greater than, less than, or equal to the target.

To keep checking the search range, we need to use a `while` loop. As long as the lowest index is less than or equal to the highest index, the search should continue.

If `nums[mid]` is equal to the target, we have found the correct index and can return it.

If `nums[mid]` is smaller than the target, we need to update `low = mid + 1`. Since `mid` is smaller than the target, we know the target cannot be before or at the current `mid`, so the next search starts at `mid + 1`. If that new position contains the target, the next comparison will find it.

If `nums[mid]` is greater than the target, we update `high = mid - 1`. Since the target cannot be after the current `mid`, the search range now ends one position before it.

The process keeps repeating by always checking the middle of the current search range and updating either `low` or `high` when necessary, until the target is found or `-1` is returned, as requested in the problem statement.

> **Note:** Before solving this exercise, I first had to learn what binary search was. After understanding how it works, I was able to solve the problem.
