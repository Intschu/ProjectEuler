import numpy as np
print("Euler problems")

def isdivisible(x, nmax): # check if x if divisible by 1, 2, ..., nmax; output c =1 if not divisible and c = 0 if divisible
    c = 0 # assume deafault divisibility (c=0) 
    j = 0
    while c==0 and j<nmax: #loop through j's from 1 to nmax 
        j +=1
        if x%j != 0: #check if x is divisible by j
            c=1 # set c=1 if not divisible
    return c

def euler5(): # find smallest number divisible by all 1, 2, ..., 20
    number = 2520 # begin at 2520, since it's the smallest number divisible by 1, 2, 3, ..., 10 
    divisible = 1 # assume not divisible
    while divisible == 1:  
        divisible = isdivisible(number, 20) #loop until divisible number is found
        ans +=1
    return ans-1

def nextcollatz(x): # generate next collatz number following x 
    if x%2 ==0.0: # x is even
        next = x/(2.0)
    else: # x is odd
        next = 3.0*x + 1.0
    return next

def collatzsequence(x): # generate list with collatz sequence staring from x
    list = []
    y = x
    while y != 1.0: # append collatz numbers until 1 is encountered
        list.append(y)
        y = nextcollatz(y)
    list.append(1.0)
    return list

def euler14(): # find which number from one to million has the ;longest collatz sequence
    length = 0 # length of the longest collatz sequence
    longest = 0.0 # number giving the lostest collatz sequence 
    j = 1000000.0
    while j != 0.0:
        temp = collatzsequence(j)
        if len(temp) > length: 
            length = len(temp)
            longest = j
        j -= 1.0
    return longest


def euler1(method=1): # find sum of all multiples of 3 and 5 below 1000
    if method == 1: #first method
        return sum(j for j in range(1000) if j%3 == 0 or j%5 == 0) 
    if method == 2: # second method
        s = 0
        for j in range(999//3):
            s += (j+1)*3
        for j in range(999//5):
            s += (j+1)*5
        for j in range(999//(3*5)):
            s -= (j+1)*3*5
        return s
    if method == 3: # third method
        return sum(j*(999//j)*(1+999//j)//2 for j in [3, 5]) - sum(j*(999//j)*(1+999//j)//2 for j in [3*5])
    else:
        print("Choose method 1, 2 or 3 as argument")
        return None

def euler2(): # find sum of even Fibonacci numbers not exceeding four million
    fib = [1, 2] # first two fibonacci numbers
    s = 2 # sum
    j = fib[-1] + fib[-2] # next finonacci number
    while j <= 4e6:
        fib.append(j) 
        if j%2 == 0: # add to sum if even
            s += j
        j = fib[-1] + fib[-2]
    return s
