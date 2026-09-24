class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        '''evencount=0
        s=sum(nums)
        leftsum=0
        rightsum=s
        for i in range(len(nums)):
            leftsum+=nums[i]
            rightsum=rightsum-nums[i]
            if abs(rightsum-leftsum)%2==0:
                evencount+=1
        return evencount'''
        s=sum(nums)
        if s%2!=0:
            return 0
        return len(nums)-1