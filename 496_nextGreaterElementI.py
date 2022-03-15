def nextGreaterElement(nums1: list, nums2: list) -> list:
    res = []
    for n in nums1: 
        i = nums2.index(n)
        if i + 1 < len(nums2): 
            if nums2[i+1] > n:
                res.append(nums2[i+1])
            else:
                res.append(-1)
        else:
            res.append(-1)
    return res

print(nextGreaterElement(nums1 = [2,4], nums2 = [1,2,3,4]))