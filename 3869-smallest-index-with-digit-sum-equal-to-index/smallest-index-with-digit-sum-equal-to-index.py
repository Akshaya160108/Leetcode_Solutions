class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        #index=-1
        for i in range(len(nums)):
            x=nums[i]
            digit=0
            while x>0:
                digit+=x%10
                x=x//10
            if digit==i:
                return i
        return -1