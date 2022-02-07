def rotate(nums:list, k:int)-> list:
    L = len(nums)
    if L == k: return

    k = k%L # the case when k > L
    nums.reverse()

    for i in range(k//2):
        nums[i], nums[k-1-i] = nums[k-1-i], nums[i]

    for i in range(k, (L+k)//2):
        nums[i], nums[L-1-i+k] = nums[L-1-i+k], nums[i]

    return nums
    
    """l = len(nums)-k
    for n in range(l):
        nums.append(nums[n])
    print(nums)
    return nums[l:]"""

print(rotate([1,2,3,4,5,6,7], 3))
