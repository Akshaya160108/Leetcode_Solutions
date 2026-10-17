class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        res=[-1,-1]
        n=len(nums)
        for i in range(n):
            for j in range(n):
                if abs(i-j)>=indexDifference and abs(nums[i]-nums[j])>=valueDifference:
                    res=[i,j]
        return res