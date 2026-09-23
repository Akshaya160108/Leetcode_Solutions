class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        d={}
        for x in digits:
            if x in d:
                d[x]+=1
            else:
                d[x]=1
        res=[]
        for i in range(100,999):
            if i%2==0:
                present=True
                s=str(i)
                for k in s:
                    k=int(k)
                    if k in d:
                        if s.count(str(k))>d[k]:
                            present=False
                            break
                    else:
                        present=False
                        break
                if present:
                    res.append(i)
        return res