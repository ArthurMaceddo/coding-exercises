# Two Sum - My Explanation

At first, I found this challenge quite difficult. I couldn't solve it without looking at other solutions first, but after understanding the logic, I was able to explain how each approach works.

The goal of this problem is to find **two numbers** in an array whose sum equals the `target` and return **their indices**.

There are three common ways to solve this problem:

- **Brute Force**
- **Two-pass Hash Table**
- **One-pass Hash Table**

---

## My First Thought

When I first tried to solve this problem, my initial idea was to compare each element with every following element in the array.

If the sum wasn't equal to the `target`, I would move to the next index and repeat the process until I found the correct pair.

In other words, my first approach was **Brute Force**, which is the easiest solution to understand. The idea is to use **two `for` loops**, testing every possible combination until finding the desired sum.

---

# Brute Force

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []
```

This is the simplest way to solve the problem.

We iterate through every possible pair using two loops and check whether the sum of the two numbers equals the `target`.

The only detail I missed when trying to solve it on my own was using `i + 1` in the second loop.

If we started from `0` every time, we would end up comparing an element with itself and repeating comparisons that had already been made.

Using `i + 1` ensures that:

- We don't compare an element with itself.
- We don't repeat pairs that have already been checked.
- We only iterate through the necessary combinations.

---

# One-pass Hash Table

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevMap = {}

        for index, item in enumerate(nums):

            diff = target - item

            if diff in prevMap:
                return [prevMap[diff], index]

            prevMap[item] = index

        return []
```

This approach uses a completely different way of thinking.

Instead of testing every possible combination, we store the numbers we've already visited in a dictionary called `prevMap`.

The dictionary follows this structure:

```python
value : index
```

For example:

```python
{
    2: 0,
    7: 1,
    11: 2
}
```

For each number in the array, we do the following:

1. Calculate the value needed to reach the `target`.

```python
diff = target - item
```

2. Check whether this value (`diff`) already exists in `prevMap`.

If it does, it means we've already encountered the number needed to complete the sum.

So we simply return both indices:

```python
return [prevMap[diff], index]
```

If the value doesn't exist yet, we store the current number and its index in the dictionary:

```python
prevMap[item] = index
```

This allows future iterations to use the current number when looking for the required complement.

---

## Conclusion

In my opinion, the **Brute Force** approach is much easier to understand, especially for beginners.

The **Hash Table** solution requires a bit more logical thinking, but it's significantly more efficient because it only traverses the array once instead of checking every possible combination.

Once you understand the idea behind `diff` and `prevMap`, the algorithm becomes much easier to visualize, and it's clear why this is considered the optimal solution for this problem.
