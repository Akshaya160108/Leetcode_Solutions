class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        ans=[]
        while len(nums)>0:
            mini=min(nums)
            maxi=max(nums)
            ans.append((mini+maxi)/2)
            nums.remove(mini)
            nums.remove(maxi)
        return min(ans)