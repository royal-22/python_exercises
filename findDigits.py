def findDigits(nums:list) -> int: 
    
    return len([n for n in nums if len(str(n)) % 2 == 0])
    """maxeven = 0
    for n in nums: 
        n = str(n)
        digits= 0
        for j in n: 
            digits += 1
        if digits%2 == 0: 
            maxeven += 1
    return maxeven"""

nums_1 = [122,3435,222,62,796]
print(findNumbers(nums_1))
