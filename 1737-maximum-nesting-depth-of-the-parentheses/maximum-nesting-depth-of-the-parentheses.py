class Solution:
    def maxDepth(self, s: str) -> int:
        res=0
        par=0
        for x in s:
            if x=='(':
                par+=1
            elif x==')':
                par-=1
            else:
                continue
            if par>res:
                res=par
        return res