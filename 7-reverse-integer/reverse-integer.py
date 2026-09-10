class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            sign=-1
        else:
            sign=1
        reverse=0
        x=abs(x)
        while x>0:
            d=x%10
            reverse=reverse*10+d
            x=x//10
        reverse*=sign
        if reverse<-2**31 or reverse>2**31-1:
            return 0
        else:
            return reverse
    
        