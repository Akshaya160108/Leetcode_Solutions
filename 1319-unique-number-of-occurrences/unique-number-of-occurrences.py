class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        d={}
        for x in arr:
            if x in d:
                d[x]+=1
            else:
                d[x]=1
        res=d.values()
        return len(res)==len(set(res))