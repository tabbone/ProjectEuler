"""
<p>A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 
$2$-digit numbers is $9009 = 91 \times 99$.</p>
<p>Find the largest palindrome made from the product 
of two $3$-digit numbers.</p>
"""

if __name__=="__main__":
    n1 = 999
    n2 = 999
    nums = [i*j for i in range(1,n1+1) for j in range(1,n2+1) if str(i*j)==str(i*j)[::-1]]
    print(max(nums))
