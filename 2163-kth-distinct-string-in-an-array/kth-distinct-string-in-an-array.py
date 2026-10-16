class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        d={}
        for ch in arr:
            if ch in d:
                d[ch]+=1
            else:
                d[ch]=1
        res=[]
        for key,value in d.items():
            if value==1:
                res.append(key)
        if k>len(res):
            return ""
        return res[k-1]