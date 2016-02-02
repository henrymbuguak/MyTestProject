'''
Created on Feb 2, 2016

@author: henry
'''

# Accept number from user and determine if it is odd or EVEN_ODD
num = input("Enter a number: ")
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")