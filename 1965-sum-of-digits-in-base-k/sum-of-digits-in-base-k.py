class Solution:
    def sumBase(self, n: int, k: int) -> int:
        #new=""
        sum=0
        while n>0:
            sum+=n%k
            #new+=str(n%k)
            n=n//k
            
        return sum