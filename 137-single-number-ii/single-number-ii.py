class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d={}
        for i in range(0,len(nums)):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        ans=0
        for k,v in d.items():
            if v==1:
                ans=k
                break
        return ans
        '''bits=[0]*32
        for i in nums:
            for j in range(32):
                if i&(1<<j):
                    bits[j]+=1
        ans=0
        for j in range(32):
            if bits[j]%3!=0:
                ans+=1<<j
        return ans'''
        