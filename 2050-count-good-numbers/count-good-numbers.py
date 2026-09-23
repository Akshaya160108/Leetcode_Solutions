class Solution:
    def countGoodNumbers(self, n: int) -> int:
        #instead of generating all the pairs and checking everything i came to a conclusion that
        #how many choices are there for each position
        #for even position 5 choices-0,2,4,6,8
        #for odd positions  4 choices of primes-2,3,5,7
        '''good=1
        mod=10**9+7
        for i in range(n):
            if i%2==0:
                good*=5
            else:
                good*=4
        return good%mod'''
        #looping n times getting tle moving to power function
        mod=10**9+7
        even=(n+1)//2
        odd=n//2
        return (pow(5,even,mod)*pow(4,odd,mod))%mod