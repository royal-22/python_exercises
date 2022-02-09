    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #s.reverse()
        
        b, e = 0, len(s)-1 #b -> beginning, e -> end
        
        while b < e: 
            s[b], s[e] = s[e], s[b]
            b+=1
            e-=1
