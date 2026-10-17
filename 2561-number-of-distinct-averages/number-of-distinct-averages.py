class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        s=set()
        nums.sort()
        n=len(nums)
        while n>0:
            s.add((nums[0]+nums[-1])/2)
            nums.remove(nums[0])
            nums.remove(nums[-1])
            n-=2
        return len(s)