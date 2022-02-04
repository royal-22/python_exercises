from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for key,value in collections.Counter(nums).items():
            if value == 1:
                return key
              
    """for count, value in enumerate(nums): 
            if nums.count(value) == 1: 
                return value"""
    
    """r = 0
    for n in nums:
        r ^= n

    return r """
            
