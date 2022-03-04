    def MissingNumber(self,array,n):
        # code here
        """missing = 1
        sorted(array)
        for i in range(n):
            if (array[i] == missing):
                missing += 1
            else: 
                return missing"""
        """a=[0 for i in range(n)]
        for i in array:
            a[i-1]=i
        p=a.index(0)
        return p+1"""
        res = (n*(n+1))//2
        for i in range(n-1):
          res -= array[i]
        return res
