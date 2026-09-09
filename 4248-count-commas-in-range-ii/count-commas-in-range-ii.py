class Solution:
    def countCommas(self, n: int) -> int:
        if n<999:
            return 0
        totalcommas=0
        start=1000
        while start<=n:
            totalcommas+=n-start+1
            start*=1000
        return totalcommas