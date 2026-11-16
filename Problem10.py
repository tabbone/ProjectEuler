"""
<p>The sum of the primes below $10$ is $2 + 3 + 5 + 7 = 17$.</p>
<p>Find the sum of all the primes below two million.</p>
"""

if __name__ == "__main__":
    primes = [2,3,5,7]
    n=8
    max_prime = 2000000
    while True:
        flag = 0
        for i in primes:
            if n % i != 0:
                flag+=1
            else:
                #if there is a prime factor, break
                flag = 0
                break
        if flag == len(primes):
            if n < max_prime:
                primes.append(n)
                print(n)
            else:
                break
        n+=1
    print(primes)
    #142913828922
    print(sum(primes))
