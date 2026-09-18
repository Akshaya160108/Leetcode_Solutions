def solve(n):
    if n==0 or n==1:
        return n
    return solve(n-1)+solve(n-2)
class Solution:
    def fib(self, n: int) -> int:
        ans=solve(n)
        return ans