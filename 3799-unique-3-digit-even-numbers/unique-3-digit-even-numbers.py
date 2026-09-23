class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        d={}
        for x in digits:
            if x in d:
                d[x]+=1
            else:
                d[x]=1
        res=[]
        for i in range(100,999,2):
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
            if present and i not in res:
                res.append(i)
        return len(res)