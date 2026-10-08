class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        n=len(nums)
        res=[]
        prefixmax=[0]*n
        suffixmax=[0]*n
        for i in range(n):
            if i%k==0:
                prefixmax[i]=nums[i]
            else:
                prefixmax[i]=max(nums[i],prefixmax[i-1])
        suffixmax[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            if i%k==k-1:
                suffixmax[i]=nums[i]
            else:
                suffixmax[i]=max(nums[i],suffixmax[i+1])
        i=k-1
        j=0
        while i<n:
            res.append(max(prefixmax[i],suffixmax[j]))
            i+=1    
            j+=1
        return res