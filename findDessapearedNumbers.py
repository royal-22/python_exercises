def findDisappearedNumbers(nums: list)->list: 
    nl = [x for x in range(1, len(nums)+1)]
    number = []

    for n in range(len(nums)): 
        if nl[n] not in nums: 
            number.append(nl[n])
    return number

print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))


def findDisappearedNumbers2(nums:list)->list: 
    begin, end = 0, len(nums)
    miss_nums = []
    numbers = set(nums)

    while begin < end: 
        if begin + 1 not in numbers: 
            miss_nums.append(begin+1)
        begin += 1
    return miss_nums

print(findDisappearedNumbers2([4,3,2,7,8,2,3,1]))


def findDisappearedNumbers3(nums:list)->list:
    return set(range(1, len(nums)+1)) - set(nums)

print(findDisappearedNumbers3([4,3,2,7,8,2,3,1]))
