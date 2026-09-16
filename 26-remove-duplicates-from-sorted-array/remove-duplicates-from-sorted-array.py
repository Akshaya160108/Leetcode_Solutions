class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result=[]
        for i in nums:
            if i not in result:
                result.append(i)
        n=len(result)
        for i in range(n):
            nums[i]=result[i]
        return n