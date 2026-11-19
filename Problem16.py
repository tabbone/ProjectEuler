"""
<p>$2^{15} = 32768$ and the sum of its digits is $3 + 2 + 7 + 6 + 8 = 26$.</p>
<p>What is the sum of the digits of the number $2^{1000}$?</p>
"""

if __name__=="__main__":
    num = 2**1000
    sum = 0
    while num > 0:
        low_order = num % 10
        print( num,low_order, sum)
        sum += low_order
        num -= low_order
        num = num // 10
    print( num,low_order, sum)

   