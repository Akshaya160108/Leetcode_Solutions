class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        res=[]
        seen=[]
        for x in nums:
            if x not in seen:
                if nums.count(x)>=k:
                    for _ in range(k):
                        res.append(x)
                else: 
                    t=nums.count(x)
                    for _ in range(t):
                        res.append(x)
                seen.append(x)
            
        return res