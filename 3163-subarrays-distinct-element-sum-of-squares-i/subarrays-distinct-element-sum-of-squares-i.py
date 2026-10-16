class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        res=0
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n+1):
                s=set(nums[i:j])
                l=len(s)
                res+=l*l
        return res