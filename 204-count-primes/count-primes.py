num=5*(10**6)
primes=[True]*num
def computesive():
    primes[0]=primes[1]=False
    i=2
    while i*i<=num:
        if primes[i]:
            for j in range(i*i,num,2):
                primes[j]=False
        i+=1

class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        primes=[True]*n
        primes[0]=primes[1]=False
        i=2
        while i*i<=n:
            if primes[i]:
                for j in range(i*i,n,i):
                    primes[j]=False
            i+=1
        return sum(primes)