# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate return values

# Add all the numbers from 0 to n
def sumOfN(n):
    total = 0
    
    for i in range(n+1):
        total = total + i

    return total

# Main processing
result = sumOfN(10) # Call the function and ASSIGN the return value to result
print("The sum of the first 10 integers is %d" %result)
