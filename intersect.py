from typing import List
def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
        c = Counter(nums1)
        result_list = []
        for n in nums2: 
            if c[n]>0:
                result_list.append(n)
                c[n] -=1
        return result_list
