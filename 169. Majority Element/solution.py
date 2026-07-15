counter = {}
n = len(nums) // 2

for num in nums:

    if num in counter:
        counter[num] = counter[num] + 1
    else:
        counter[num] = 1

    if counter[num] > n:
        return num