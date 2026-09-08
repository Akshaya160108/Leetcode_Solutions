class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        res=[]
        for x in nums:
            if -x in nums:
                res.append(abs(x))
        if len(res)>=1:
            return max(res)
        return -1