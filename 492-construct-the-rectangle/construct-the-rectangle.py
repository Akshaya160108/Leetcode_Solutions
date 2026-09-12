class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        res=[]
        l=1
        while l*l<=area:
            w=area//l
            if w>=l:
                res.append([l,w])
            l+=1
        ans=float('inf')
        mini=float('inf')
        for x in res:
            l,w=x[0],x[1]
            if l*w==area and abs(w-l)<mini:
                mini=abs(w-l)
                ans=[w,l]
        return ans
