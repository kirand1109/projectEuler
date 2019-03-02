'''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000 '''

import math

sum=0


for i in range (1,1000):

# checking the number is either multiple of 3 or 5 and assign that number to m_3_5 variable
    if (i%3==0) or (i%5==0):
        m_3_5=i
        sum=sum+m_3_5

        
print sum
