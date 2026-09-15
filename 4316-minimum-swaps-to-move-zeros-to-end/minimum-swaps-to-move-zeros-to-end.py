class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        n=len(nums)
        count=0
        i=0
        j=n-1
        while i<j:
            if nums[i]==0 and nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                count+=1
                i+=1
                j-=1
            elif nums[i]!=0:
                i+=1
            else:
                j-=1
        return count