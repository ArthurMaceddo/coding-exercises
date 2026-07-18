def intersection(nums1, nums2):
    newSet = set(nums1)
    newSet2 = set(nums2)
    return list(newSet & newSet2)