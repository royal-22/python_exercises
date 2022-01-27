def removeDuplicates(nums:list)->list:
    if len(nums) == 0: 
        return 0

    k = 0
    for n in range(len(nums)): 
        if nums[n] != nums[k]:
            k+=1
            nums[k] = nums[n]
    return k +1

def removeDuplicates(nums:list)->list: 
    set_ = set()
    for n in nums:
        set_.add(n)
    nums.clear()

    for item in sorted(set_): 
        nums.append(item)
    return len(set_)
