"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

source: https://leetcode.com/problems/search-insert-position/
"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)): 
            if (nums[i] >= target):
                return i
        return len(nums) 

      
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = (low + high) // 2
            currentItem = nums[mid]

            if currentItem == target:
                return mid
            elif currentItem < target:
                low = mid + 1
            else:
                high = mid - 1
        return low
     
