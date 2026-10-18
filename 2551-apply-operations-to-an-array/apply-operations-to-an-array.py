class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        n=len(nums)
        i=0
        j=i+1
        while j<n:
            if nums[i]==nums[j]:
                nums[i]=nums[i]*2
                nums[j]=0
            i+=1
            j+=1
        res=[]
        count=0
        for x in nums:
            if x!=0:
                res.append(x)
            else:
                count+=1  
        for i in range(count):
            res.append(0)
        return res      