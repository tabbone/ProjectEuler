"""
<p>The prime factors of $13195$ are 
$5, 7, 13$ and $29$.</p>
<p>What is the largest prime factor of the number 
$600851475143$?</p>
"""


if __name__ == "__main__":
    n=600851475143
    #n=13195
    factors = []
    d=2
    while d*d <= n:
        while n % d == 0:
            factors.append(d)
            n=n//d
        d+=1
    if n > 1:
        factors.append(n)
    print( max(factors) )