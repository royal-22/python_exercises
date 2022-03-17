class Solution:
    def intToRoman(self, num: int) -> str:
        numbers = [1, 4, 5, 9,
                   10, 40, 50, 90,
                   100, 400, 500, 900, 
                   1000]
        romanNums = ['I', 'IV', 'V', 'IX',
                     'X', 'XL', 'L', 'XC',
                     'C', 'CD', 'D', 'CM',
                    'M']
        
        quantity = 0
        roman = ""
        i = 12
        
        while num: 
            
            quantity = num//numbers[i]
            num %= numbers[i]
            
            while quantity: 
                
                roman += romanNums[i]
                quantity -= 1
                
            i -= 1
            
        return roman
