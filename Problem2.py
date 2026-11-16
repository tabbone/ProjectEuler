"""
<p>Each new term in the Fibonacci sequence is generated 
by adding the previous two terms. By starting with $1$ 
and $2$, the first $10$ terms will be:
$$1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...$$</p>
<p>By considering the terms in the Fibonacci 
sequence whose values do not exceed four million, 
find the sum of the even-valued terms.</p>
"""

if __name__ == "__main__":
    fibs=[1,2]
    ans = 2
    i = 2
    while fibs[i-1]+fibs[i-2] < 4000000:
        latest_fib = fibs[i-1]+fibs[i-2]
        fibs.append(latest_fib)
        if latest_fib %2 ==0:
            ans += latest_fib
        i+=1
    print(ans)
    print(fibs)