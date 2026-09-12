class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0:
            return "0"
        arr=[]
        if num<0:
            sign=-1
        else:
            sign=1
        num=abs(num)
        while num>0:
            arr.append(str(num%7))
            num=num//7
        res="".join(arr)[::-1]
        if sign==-1:
            res=int(res)*sign
        return str(res)