class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        m=len(nums)
        for i in range(1<<m):
            ans=[]
            for j in range(m):
                if (i&(1<<j)):
                    ans.append(nums[j])
            res.append(ans)
        return res