class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevMap = {}

        for index, item in enumerate(nums):

            diff = target - item

            if diff in prevMap:
                return [prevMap[diff], index]

            prevMap[item] = index

        return []