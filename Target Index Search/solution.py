def binarySearch(nums, target):
    low = 0
    mid = 0
    high = len(nums)-1

    while low <= high:
       
        mid = (low + high)// 2

        if nums[mid] < target:
           low = mid + 1

        elif nums[mid] == target:
            return mid
       
        else:
           high = mid - 1
    
    return -1
       


if __name__ == '__main__':
    nums_count = int(input().strip())

    nums = []

    for _ in range(nums_count):
        nums_item = int(input().strip())
        nums.append(nums_item)

    target = int(input().strip())

    result = binarySearch(nums, target)

    print(result)
