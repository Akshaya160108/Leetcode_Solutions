class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        n=x
        num=0
        while n>0:
            num+=n%10
            n=n//10
        if x%num==0:
            return num
        return -1