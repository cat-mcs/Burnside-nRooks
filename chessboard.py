
import numpy as np 
import math as mth

max = int(input("Enter max dimension: "))
natural = np.arange(5,max)

def involution(num):
    
    m = 0 
    j = 1 
    k = 0 

    if num == 0 or num == 1:
        return 1 
    
    i = [1,1]
    while m < num:
        InvNo = i[j] + m*i[k]
        i.append(InvNo)
        j += 1
        k += 1
        m=m+1 
    return i[-1]



def rotate90(num,r):

    if r == 0:
        p = 2
    if r == 1:
        p = 3
    else: 
        return 0
    
    ii = []
    k = 0 
    
    while num > p + 4*k:
        term = num - (p + 4*k)
        ii.append(term)
        k = k + 1

    return mth.prod(ii)


def rotate180(num,r):
    
    if r == 0 or r == 2:
        p = 0
    if r == 1 or r == 3:
        p = 1
        
    ii = []
    k = 0

    while num > p + 2*k:
        term = num - (p + 2*k) 
        ii.append(term)
        k = k + 1

    return mth.prod(ii)

for n in natural:

    print(n)

    nfact = mth.factorial(n)
    t = mth.floor(n/4)
    r = n%4

    noInvs = involution(n)
    prod90 = rotate90(n,r)
    prod180 = rotate180(n,r)

    configCount = 1/8 * (nfact + 2*noInvs + 2*prod90 + prod180)
    print("The number of configurations is: ", configCount)

print("terminating...")