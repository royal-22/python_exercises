class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for n in nums:
            product *= n
        if product > 0: 
            return 1
        elif product < n:
            return -1
        return 0
