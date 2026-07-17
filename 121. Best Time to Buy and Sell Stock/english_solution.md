# Best Time to Buy and Sell Stock (LeetCode 121)

This looked like an easy problem at first, but it ended up taking me much longer than I expected.

My first solution was a **brute-force approach**, since it was the most straightforward idea I could think of. After struggling for a while, I watched a video explaining the problem. I had already looked at the official LeetCode solution, but I couldn't understand the reasoning behind it. The video was what finally made everything click.

My first implementation has a time complexity of **O(n²)**. It doesn't meet the efficiency requirements of the problem and doesn't pass all LeetCode test cases, but I think it would still be enough to explain my reasoning during an interview.

---

# My First Solution (Brute Force)

```python
max_profit = 0

for i in range(len(prices)):
    for j in range(i + 1, len(prices)):
        profit = prices[j] - prices[i]

        if profit > max_profit:
            max_profit = profit

return max_profit
```

## How does this solution work?

We use two nested loops:

* `i` represents the day we buy the stock.
* `j` represents a possible day to sell it.

For every possible pair, we calculate the profit:

```python
profit = prices[j] - prices[i]
```

If the current profit is greater than the best profit we've seen so far, we update `max_profit`.

Since `max_profit` starts at `0`, we'll never return a negative profit.

### Complexity

* **Time:** `O(n²)` ❌
* **Space:** `O(1)` ✅

---

## Video that helped me

This was the video that finally helped me understand the problem:

https://www.youtube.com/watch?v=kJZrMGpyWpk

---

# Optimized Solution

```python
min_price = float('inf')
max_profit = 0

for price in prices:

    if price < min_price:
        min_price = price

    profit = price - min_price

    if profit > max_profit:
        max_profit = profit

return max_profit
```

## Why use `float('inf')`?

We initialize `min_price` with positive infinity because we want **every price in the array to be smaller than the initial value**.

This guarantees that the first price becomes our initial minimum.

---

## How does this solution work?

As we iterate through the array only once:

1. Check whether we've found a new minimum price.

```python
if price < min_price:
    min_price = price
```

2. Calculate the profit if we sold the stock today.

```python
profit = price - min_price
```

3. If this profit is larger than the best profit seen so far, update `max_profit`.

```python
if profit > max_profit:
    max_profit = profit
```

---

## Example

For the array:

```text
[7, 1, 5, 3, 6, 4]
```

The values evolve like this:

| Current Profit | Maximum Profit |
| -------------: | -------------: |
|              0 |              0 |
|              0 |              0 |
|              4 |              4 |
|              2 |              4 |
|              5 |              5 |
|              3 |              5 |

At the end, we return:

```python
5
```

---

# The Key Idea

The most important sentence to remember for this problem is:

> **Always keep track of the lowest price seen so far.**

During each iteration, ask yourself three questions:

1. **Is this the lowest price I've seen so far?**

   * Yes → Update `min_price`.

2. **If I sold today, what would my profit be?**

```python
profit = price - min_price
```

3. **Is this the highest profit I've seen so far?**

   * Yes → Update `max_profit`.

---

## Complexity

* **Time:** `O(n)` ✅
* **Space:** `O(1)` ✅

This solution traverses the array only once and is the expected approach for this LeetCode problem.
