"""
<p>By listing the first six prime numbers: $2, 3, 5, 7, 11$, 
and $13$, we can see that the $6$th prime is $13$.</p>
<p>What is the $10,001$st prime number?</p>
"""

if __name__ == "__main__":
    primes = [2,3,5,7,11,13,17]
    n = 18

    while len(primes) != 10001:
        flag = 0
        for i in primes:
            if n % i != 0:
                flag+=1
        if len(primes)==flag:
            primes.append(n)
        n+=1      
    print(primes[10000])  
        

        