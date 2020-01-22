"""
Created on Wed Jan 22 11:15:01 2020

@author: Ryan.Worth
"""

## 

## find multiples of 3 or 5 
ans = [x for x in range(1000) if (x % 3 == 0 or x % 5 == 0)]
print (ans)

## sum them
print (sum(ans))

## answer = 233168

