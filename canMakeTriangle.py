class Solution:
    def canMakeTriangle(self, A, N): 
        #code here
        res = [] 
        for i in range(N-2):
            a = A[i]
            b = A[i+1]
            c = A[i+2]
            if a+b > c and a+c>b and b+c>a:
                res.append(1)
            else: 
                res.append(0)
        return res
