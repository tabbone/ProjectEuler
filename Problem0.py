"""
A number is a perfect square, or a square number, if it is the square of a positive integer.
For example,  is a square number because    ; it is also an odd square.

The first 5 square numbers are: , and the sum of the odd squares is    .

Among the first 272 thousand square numbers, what is the sum of all the odd squares?
"""

if __name__ == "__main__":
    n = 272000
    sum = 0
    for i in range(1,n+1):
        sq = i*i
        if sq % 2 != 0: 
            sum= sum+sq
    print(sum)
