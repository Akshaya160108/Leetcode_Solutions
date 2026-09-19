class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        d={}
        s=str(n)
        for x in s:
            if x in d:
                d[x]+=1
            else:
                d[x]=1
        score=0
        for k,x in d.items():
            score+=int(k)*x
        return score