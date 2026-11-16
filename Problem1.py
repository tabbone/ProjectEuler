"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6, 9 The sum of these multiples is 23.

Find the sum of all the multiples of  3 or 5  below 1000.
"""

if __name__ == "__main__":
    sum = 0
    ceil = 1000
    for i in range(1,ceil):
        if i%3 == 0 or i%5 == 0:
            sum += i
    print(sum)
