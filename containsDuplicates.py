def containsDuplicate(nums:list)->bool:
    hashset = set()
    for n in nums: 
        if n in hashset:
            return True
        hashset.add(n)
    return False
    """return len(set(nums)) != len(nums)"""
    
    """i = 0
    value = False
    while i < len(nums): 
        if nums.count(nums[i]) > 1: 
            value = True
            break
        i+=1

    return value
"""
print(containsDuplicate([1,2,3,4]))
