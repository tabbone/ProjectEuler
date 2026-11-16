"""
<p>$2520$ is the smallest number that can be divided by 
each of the numbers from $1$ to $10$ without any 
remainder.</p>
<p>What is the smallest positive number that is 
<strong class="tooltip">evenly divisible
<span class="tooltiptext">
divisible with no remainder</span></strong> 
by all of the numbers from $1$ to $20$?</p>
"""


if __name__ == "__main__":
    num = 1
    r = range(11,21)
    while True:
        flag = 0
        for i in r:
            flag += num % i
        if flag == 0:
            print(num)
            break
        num += 1
    
