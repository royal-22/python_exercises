    def sortArrayByParity(nums: List[int]) -> List[int]:
        even = [x for x in nums if x%2==0]
        odd = [x for x in nums if x%2!=0]
        nums = even + odd
        return nums
