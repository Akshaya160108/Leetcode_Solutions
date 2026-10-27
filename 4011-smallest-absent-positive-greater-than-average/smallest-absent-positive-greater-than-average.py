class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        n=len(nums)
        s=sum(nums)
        avg=s//n
        if avg>0:
            i=avg+1
        else:
            i=1
        while True:
            if i not in nums:
                return i
            i+=1