def findKDistantIndices(nums, key, k):
    indexes = [x for x in range(len(nums)) if nums[x] == key]
    res = set()
    
    for idx in range(len(nums)):
        for num in indexes:
            if abs(idx - num) <= k:
                res.add(idx)
    return sorted(list(res))

print(findKDistantIndices(nums = [2,2,2,2,2], key = 2, k = 2))