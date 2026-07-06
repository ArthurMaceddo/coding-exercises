# Explanation

The goal of this problem is to remove duplicate values from the sorted array `nums` **in-place**, keeping only one occurrence of each number.

```python
k = 1

for i in range(1, len(nums)):
    if nums[i] != nums[k - 1]:
        nums[k] = nums[i]
        k += 1

return k
```

## What do `i` and `k` represent?

- **`i`** → Iterates through every element in the array (**read pointer**).
    
- **`k`** → Indicates the position where the next unique element should be stored (**write pointer**).
    

## Reasoning

My first thought was that I needed to iterate through every element of the array.

I couldn't start at index `0` because I would need to compare the current element with the previous one. If I started at `0`, the comparison would involve index `-1`, which is not what we want for this algorithm.

The idea is simple:

- Compare the current element with the last unique element stored.
    
- If they are different, copy the current element to `nums[k]`.
    
- Increment `k` so it points to the next available position.
    
- At the end, return `k`, which represents the number of unique elements in the array.
    

## Example

```text
nums = [0,0,1,1,1,2,2,3,3,4]

k = 1

i = 1 -> 0 == 0 -> Skip
i = 2 -> 1 != 0 -> nums[1] = 1, k = 2
i = 3 -> 1 == 1 -> Skip
i = 4 -> 1 == 1 -> Skip
i = 5 -> 2 != 1 -> nums[2] = 2, k = 3
...
```

Final array:

```text
[0,1,2,3,4,_,_,_,_,_]
```

The first `k` positions contain all unique values in sorted order.

