class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count=0
        for x in nums:
            s=str(x)
            if len(s)%2==0:
                count+=1
        return count