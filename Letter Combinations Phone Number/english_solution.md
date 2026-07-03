# Explanation

Resolved Date: 06/27/2026

- We create the **telephone** dictionary containing the mappings from digits **2** to **9**, while also including **0** and **1**.

- We create an empty list where all combinations will be stored.

- We create a function called `backtracking` with the parameters `index` and `char`:
  - `index` = the current position of the digit being processed.
  - `char` = the combination built so far.

- We create an `if` statement to determine when a combination should be added to the list.

- In this case, `index` must be equal to the length of `digits` (since `digits` is a string).

- When this happens, we add the current combination to the list using `append(char)`.

- We then use `return` to end the current recursive call and return execution to the previous call.

- We create a `for` loop to iterate through each possible letter:

```python
for c in telephone[digits[index]]:
```

- This allows us to get the current digit and iterate through every letter mapped to it.

- Inside the `for` loop, we call the `backtracking` function again, increasing `index` by **1** and appending the current letter `c` to `char`.

- Why do we do this? Because recursion needs to move to the next digit. A combination is only added after every digit has been processed.

- First, the loop processes the first digit (`2`, example: `23`) and gets its corresponding letters (`a`, `b`, `c`).

- Then it calls `backtracking(1, "a")`.

- It checks the `if` condition, but the number of processed digits is still smaller than the length of `digits`.

- A new `for` loop starts, this time processing the second digit (`3`, example: `23`) and its corresponding letters (`d`, `e`, `f`).

- It calls `backtracking` again (which currently has `index = 1` and `char = "a"`), increases the index by **1**, and appends `"d"` to the current string.

- At this point, the recursive call becomes:

```python
backtracking(1 + 1, "a" + "d")
backtracking(2, "ad")
```

- Now, when the `if` statement is checked again, `index` is equal to the length of `digits`.

- The combination `"ad"` is added to the list.

- The function returns to the previous recursive call (`backtracking(1, "a")`).

- The `for` loop still has more letters to process (`e` and `f`), so the same process repeats.

- After all letters from `"def"` have been processed, execution returns to the first `for` loop, which was paused while processing `"a"`.

- The next letter becomes `"b"`, and the entire process repeats until every possible combination has been generated.

- Finally, we call the function to define where the recursion starts:

```python
backtracking(0, "")
```

- At the end, we return `combinations`, which contains every possible letter combination.

---

# Backtracking Template

```python
def backtrack(state):

    if finished:
        save_answer()
        return

    for choice in possible_choices:
        make_choice()
        backtrack(new_state)
```

---

# Recursion Tree

```text
backtrack(0, "")

├── backtrack(1, "a")
│   ├── backtrack(2, "ad") ✓
│   ├── backtrack(2, "ae") ✓
│   └── backtrack(2, "af") ✓
│
├── backtrack(1, "b")
│   ├── backtrack(2, "bd") ✓
│   ├── backtrack(2, "be") ✓
│   └── backtrack(2, "bf") ✓
│
└── backtrack(1, "c")
    ├── backtrack(2, "cd") ✓
    ├── backtrack(2, "ce") ✓
    └── backtrack(2, "cf") ✓
```
