# average_function.py
# For this exercise the pseudo-code is required (in this same file)
# Write a function that calculates the average of the values of
# any vector of 10 numbers
# Each single value of the vector should be read from the keyboard
# and added to a list.
# Print the input vector and its average
# Define separate functions for the input and for calculating the average

'''
pseudo-code:
-for 10 times:
    -get the input for then numbers via the command line using input
    -insert it in an array
-compute the average over this array using sum/length
-print the array
-print the average
'''

import math

def ten_elements_avg():
    n = get_numbers(10)
    a = average(n)
    print("This is the input list: %s" % n)
    print("This is the average: %s" % a)

# get n numbers as input from the command line
def get_numbers(n):
    numbers = []
    for i in range(0,n):
        x = input("please type input #%s: " % int(i+1))
        numbers.insert(i,x)
    return numbers

# compute the average value of a list of numbers. cast to float for exact division
def average(x):
    return sum(x) / float( len(x) )
