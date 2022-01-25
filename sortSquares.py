from typing import List

def sortedSquares(nums: List[int]) -> List[int]:
        l_list = [n * n for n in nums]
        l_list.sort()
        return l_list
