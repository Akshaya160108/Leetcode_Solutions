class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            index=0
            for i in nums:
                if(i<target):
                    index+=1
            return index