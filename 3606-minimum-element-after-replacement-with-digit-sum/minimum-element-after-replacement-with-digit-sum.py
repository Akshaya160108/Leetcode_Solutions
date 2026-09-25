class Solution:
    def minElement(self, nums: List[int]) -> int:
        res=[]
        for x in nums:
            n=x
            s=0
            while n>0:
                s+=n%10
                n=n//10
            res.append(s)
        return min(res)