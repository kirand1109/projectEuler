'''The series, 11 + 22 + 33 + ... + 1010 = 10405071317.Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.'''

import sys, os, math

sum=0
for i in range (1, 1001):

    x=i**i
    sum=sum+x

# converting integer to string
num=str(sum)

#printing last 10 digits
print num[-10:]


