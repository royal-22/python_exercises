def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 
        respectively.

        Merge nums1 and nums2 into a single array sorted in non-decreasing order.}
        nums1 has a length of m + n
        """
        for i in range(n): 
            nums1[i+m] = nums2[i]
    
        nums1.sort()
