"""
<p>The sum of the squares of the first ten natural numbers is,</p>
$$1^2 + 2^2 + ... + 10^2 = 385.$$
<p>The square of the sum of the first ten natural numbers is,</p>
$$(1 + 2 + ... + 10)^2 = 55^2 = 3025.$$
<p>Hence the difference between the sum of the squares of the 
first ten natural numbers and the square of the sum 
is $3025 - 385 = 2640$.</p>
<p>Find the difference between the sum of the squares of the 
first one hundred natural numbers and the square of the sum.</p>
"""

if __name__== "__main__":
    sum_of_sq = 0
    for i in range(1,101):
        sum_of_sq += i*i
        print(i,i*i,sum_of_sq )
    sq_of_sum = (100/2*(1+100)) ** 2
    d = sum_of_sq - sq_of_sum
    print( sum_of_sq, sq_of_sum ,d)
