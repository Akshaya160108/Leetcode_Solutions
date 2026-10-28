class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        d={}
        for x in nums:
            if x in d:
                d[x]+=1
            else:
                d[x]=1
        for k,v in d.items():
            if v==1 and k%2==0:
                return k
        return -1