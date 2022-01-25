def majorityElement(nums: list) -> int:

    count = 0                                    
    number = 0                                
        
    for i in nums:
        if count == 0:                           
            number = i
            count += 1           
		   
        elif i == number:                     
            count += 1
        else:
            count -= 1       
    return number


numeros = [3, 1, 1, 1, 3, 3, 3]

print(majorityElement(numeros))
