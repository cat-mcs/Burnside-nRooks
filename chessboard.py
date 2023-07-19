
# importing libraries
import numpy as np 
import math as mth

# request user input
max = int(input("Enter max dimension: "))
# list of number from 5 up to user input
natural = np.arange(5,max)

# number of involutions for some n
def involution(num):

    # counters
    m = 0 
    j = 1 
    k = 0 

    # for n = 0,1 return 1
    if num == 0 or num == 1:
        return 1 

    # list for storing involution numbers for recursion
    i = [1,1]

    # while counter less than n
    while m < num:

        # recursive formula for calculating involution count
        InvNo = i[j] + m*i[k]
        # append outcome to list
        i.append(InvNo)
        # increase counters
        j += 1
        k += 1
        m=m+1 

    # return the last element in list
    return i[-1]


# number of configurations fixed by 90 degree rotation of the board
def rotate90(num,r):

    # if board dimension modulo 4 is 0 or 1
    if r == 0:
        p = 2
    if r == 1:
        p = 3
    # if board dimension modulo 4 is 2 or 3
    else: 
        return 0

    # define list for storing terms of formula
    ii = []
    # counter
    k = 0 

    # while terms of the formula are positive
    while num > p + 4*k:

        # applying formula and append result
        term = num - (p + 4*k)
        ii.append(term)
        # increase counter
        k = k + 1

    # return the product of the terms in list
    return mth.prod(ii)

# number of configurations fixed by 180 degree rotation of the board
def rotate180(num,r):

    # if board dimension modulo 4 is 0 or 2
    if r == 0 or r == 2:
        p = 0
    # if board dimension modulo 4 is 1 or 3
    if r == 1 or r == 3:
        p = 1

    # define list for storing terms of the formula
    ii = []
    # counter
    k = 0

    # while terms of the formula are positive
    while num > p + 2*k:

        # applying formula and append result
        term = num - (p + 2*k) 
        ii.append(term)
        # increase counter
        k = k + 1

    # return the product of the terms in list
    return mth.prod(ii)

# for each natural number in our list
for n in natural:

    # print the number
    print(n)

    # calculate factorial of n
    nfact = mth.factorial(n)
    # calculate n modulo 4
    r = n%4

    # call the functions above for n and r
    noInvs = involution(n)
    prod90 = rotate90(n,r)
    prod180 = rotate180(n,r)

    # use Burnsides Lemma to calculate count
    configCount = 1/8 * (nfact + 2*noInvs + 2*prod90 + prod180)
    # print the outcome
    print("The number of configurations is: ", configCount)

print("terminating...")
