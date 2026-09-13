class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digitsum=0
        squaresum=0
        while n>1:
            d=n%10
            digitsum+=d
            squaresum+=d**2
            n=n//10
        if squaresum-digitsum>=50:
            return True
        return False