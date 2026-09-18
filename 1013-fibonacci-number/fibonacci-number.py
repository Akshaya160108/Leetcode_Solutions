class Solution:
    def fib(self, n: int) -> int:
        first=0
        second=1
        next=0
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            i=2
            while i<=n:
                next=first+second
                first,second=second,next
                i=i+1
            return next
        