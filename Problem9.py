"""
<p>A Pythagorean triplet is a set of three natural numbers, 
$a < b < c$, for which,
$$a^2 + b^2 = c^2.$$</p>
<p>For example, $3^2 + 4^2 = 9 + 16 = 25 = 5^2$.</p>
<p>There exists exactly one Pythagorean triplet 
for which $a + b + c = 1000$.
<br>Find the product $abc$.</p>
"""


def pythagorian_triplet(n):
    #using return instead of brak will break all for loops
    for a in range(1,n):
        for b in range(1,n):
            for c in range(1,n):
                if a**2 + b**2 == c**2 and a+b+c == n and a < b < c:
                    return (a,b,c)
    


if __name__ == "__main__":
    (a,b,c) = pythagorian_triplet(1000)
    print(a,b,c,a*b*c)