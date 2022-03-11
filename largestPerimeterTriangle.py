class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1, 1, -1):
            a, b, c = nums[i-2], nums[i-1], nums[i]
            if (c<b+a):
                return a+b+c
        return 0
