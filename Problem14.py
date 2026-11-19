"""
<p>The following iterative sequence is defined for the set of positive integers:</p>
<ul style="list-style-type:none;">
<li>$n  n/2$ ($n$ is even)</li>
<li>$n  3n + 1$ ($n$ is odd)</li></ul>
<p>Using the rule above and starting with $13$, we generate the following sequence:
$$13  40  20  10  5  16  8  4  2  1.$$</p>
<p>It can be seen that this sequence (starting at $13$ and finishing at $1$) contains $10$ terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at $1$.</p>
<p>Which starting number, under one million, produces the longest chain?</p>
<p class="note"><b>NOTE:</b> Once the chain starts the terms are allowed to go above one million.</p>

"""

def colaz_count(n,count):
    if n!= 1:
        if n%2 == 0:
            return colaz_count(n/2,count+1)
        else:
            return colaz_count(n*3+1,count+1)
    else:
        return count+1

if __name__=="__main__":
    max = 0
    max_i=0
    for i in range(1,1000000): 
        n = colaz_count(i,0)
        if max < n:
            max = n
            max_i = i
    print(max_i, max)
    
        