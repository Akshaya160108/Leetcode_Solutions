class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        d={}
        for x in str(n):
            if x in d:
                d[x]+=1
            else:
                d[x]=1
        mini=float('inf')
        digit=float('inf')
        for k,v in d.items():
            if v<mini:
                digit=int(k)
                mini=v
            elif v==mini:
                digit=min(digit,int(k))
        return digit
        