class Solution:
    def mySqrt(self, x: int) -> int:
        """return int(sqrt(x))
                i = 1"""
        j = x
        ans = 0
        while i <= j:
            mid = (i+j)//2
            if mid <= (x//mid):
                i = mid+1
                ans = mid
            else:
                j = mid-1
        return ans
