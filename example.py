class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        
        def binary_search(left, right, target):
            
            while left <= right:
                
                middle = (left + right) // 2
                
                if arr[middle] == target:
                    return True
                elif arr[middle] < target:
                    left = middle+1
                else:
                    right = middle-1
                    
            return False 
        
        for idx in reversed(range(1, len(arr))):
            
            if arr[idx] < 0:
                break
            
            if arr[idx] % 2 == 1:
                continue
                
            target = arr[idx] // 2
            
            if binary_search(0, idx-1, target):
                return True
            
        for idx in range(0, len(arr)-1):
            
            if arr[idx] > 0:
                break
                
            if arr[idx] % 2 == 1:
                continue
                
            target = arr[idx] // 2
            
            if binary_search(idx+1, len(arr)-1, target):
                return True 
            
        return False 
