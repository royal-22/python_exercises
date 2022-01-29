arr = [0, 1, 2, 0]


def removeZeros(nums:list)->list: 
    if len(nums) < 1:
        return
    j = 0
    for num in nums:
        if num != 0:
            nums[j] = num
            j += 1
    for i in range(j, len(nums)):
        nums[i] = 0
    return nums


    """arr.sort(key=lambda x: x!=0, reverse=True)
    n = 0
    while True:
        if arr[n] == 0: 
            break
        n+=1
    print(arr[:n])
    print(n)"""

print(removeZeros(arr))

def removeZeros2(nums:list)->list: 
    zeros = [x for x in nums if x == 0]
    no_zeros = [x for x in nums if x != 0]
    #for _ in range(len(nums)):
    #    nums.pop()
    #nums.extend(no_zeros + zeros)
    nums = no_zeros + zeros
    return nums

print(removeZeros2(arr))
