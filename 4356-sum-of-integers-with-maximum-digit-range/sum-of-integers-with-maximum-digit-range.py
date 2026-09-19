class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        res=[]
        for x in nums:
            s=str(x)
            res.append(int(max(s))-int(min(s)))
        maxi=max(res)
        digitsum=0
        for i in range(len(nums)):
            if res[i]==maxi:
                digitsum+=nums[i]
        return digitsum