class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        d={}
        for word in s1.split():
            if word in d:
                d[word]+=1
            else:
                d[word]=1
        for word in s2.split():
            if word in d:
                d[word]+=1
            else:
                d[word]=1
        res=[]
        for k,v in d.items():
            if v==1:
                res.append(k)
        return res