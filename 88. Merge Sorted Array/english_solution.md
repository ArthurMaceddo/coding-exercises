## First Approach

```python
nums1[:] = sorted(nums1[:m] + nums2[:n])
```

This was my first idea for solving the problem.

I had to look up how to slice a list up to a specific position and learned that `[:m]` returns only the first `m` elements of the list.

After that, I ran into another issue. I didn't know how to modify the original list instead of making `nums1` reference a new one. After some research, I discovered that using `nums1[:]` replaces the contents of the existing list, which is exactly what LeetCode expects.

Although this solution works and is accepted, it is not the most efficient approach because it relies on `sorted()`. The expected solution uses the **Two Pointers** technique, resulting in better time and space efficiency.

# Correct Solution

In this problem, we use three pointers:

* `i`: points to the last valid element in `nums1`.
* `j`: points to the last element in `nums2`.
* `k`: points to the last available position in `nums1`, where the largest element from the current comparison will be placed.

The key insight is to traverse both arrays **from right to left**. By doing this, we take advantage of the empty spaces at the end of `nums1` and avoid overwriting values that haven't been compared yet. If we processed the arrays from left to right, we could overwrite important elements in `nums1` before using them.

The `while` loop only checks whether `j >= 0` because our goal is to copy every element from `nums2` into `nums1`. If `nums2` is exhausted first, the remaining elements in `nums1` are already in their correct positions.

Inside the loop, we check whether `i < 0` or if the current element in `nums2` is greater than the current valid element in `nums1`.

If either condition is true, the largest remaining value comes from `nums2`. We copy `nums2[j]` into `nums1[k]` and decrement `j` since that element has already been placed.

Otherwise, the largest remaining value is already in `nums1`. In that case, we copy `nums1[i]` into `nums1[k]` and decrement `i`, since that element has also been processed.

At the end of every iteration, we decrement `k` because the current position has been filled and we can move on to the next available slot.

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if i < 0 or nums2[j] > nums1[i]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1

            k -= 1
```

## Complexity

* 🟢 **Time:** `O(m + n)`
* 🟢 **Space:** `O(1)`
