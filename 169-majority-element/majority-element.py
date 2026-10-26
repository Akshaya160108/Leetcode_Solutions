class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n=len(nums)
        major=n//2
        d={}
        for x in nums:
            if x in d:
                d[x]+=1
            else:
                d[x]=1
        for k,v in d.items():
            if v>major:
                return k