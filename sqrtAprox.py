#! usr/bin/env python

#   K. M. Short
#   Math180 Numerical Analysis
#   Mills Fall 2014
#   HWK#1: Binary Search and Bisection Algorithms: Square Root Approximation
#   sqrtAprox.py



#   imports
import sys
import csv
import math


#   define Array
vals = []

#   initialize Vars
n = 0
itr = 0
root = 0
sqRoot = 0
aprxRoot = 0
floor = 0
ceiling = 0
midpoint = 0
nextMidpoint = 0
sqMidpoint = 0
midDistance = 0
toleranceVal = 0
tolerance = 0
error = 0



#  Ask the user for the integer value of the randicandn =  raw_input("Enter the integer value of the wanted square root: ")
n = raw_input("Please enter a positive integer value for the radicand: ")
print "The root which will be approximated is: " + str(n) + "."
n = float(n)



#   define Vars
sqRoot = float(math.sqrt(n))
aprxRoot = float(aprxRoot)
floor = math.floor(sqRoot)
ceiling = math.ceil(sqRoot)
midpoint = float((floor + ceiling)/2)
sqMidpoint = float(math.pow(midpoint, 2))
itr = itr + 1
midDistance = float(math.fabs(midpoint - nextMidpoint))


#   Prompt user for tollerance integer
toleranceVal = raw_input("Please enter a positive integer value for the tolerance: ")
toleranceVal = float(toleranceVal)
tolerance = float(math.pow(10, -(toleranceVal)))
print "The root will be approximated with tolerance of :" + str(tolerance) + "."


#   Print some starting values to test
print "n = " + str(n)
print "itr = " + str(itr)
print "floor = " + str(floor)
print "ceiling = " + str(ceiling)
print "midpoint = " + str(midpoint)
print "sqMidpoint = " + str(sqMidpoint)
print "midDistance = " + str(midDistance)
print "toleranceVal = " + str(toleranceVal)
print "tolerance = " + str(tolerance)
print "sqRoot = " + str(sqRoot)
print "aprxRoot = " + str(aprxRoot)



#   definition for the root approximation
def findRoot(n, itr, floor, ceiling, midpoint, sqMidpoint, midDistance, tolerance, sqRoot, aprxRoot):
    
    print "Starting Iteration Sequence!" 
    
    with open(aprxSquareCSV.csv, 'w') as f:
        f.write('n', 'itr', 'floor', 'ceiling', 'midpoint', 'sqMidpoint', 'midDistance', 'tolerance', 'aprxRoot')

    while (midDistance > tolerance):
        print "Iteration#: " + str(itr)
        midTemp = 0     #temp var to hold midpoint

        if (sqMidpoint < sqRoot):
            midTemp = midpoint
            floor = midpoint
            float(nextMidpoint = (floor + ceiling)/2)
            sqNextMidpoint = math.pow(nextMidpoint, 2)
            midpoint = nextMidpoint
            sqMidpoint = sqMidpoint
            aprxRoot = midpoint
            midDistance = midDistance
            f.write(str(n), str(itr), str(floor), str(ceiling), str(midpoint), str(sqMidpoint), str(midDistance), str(tolerance), str(aprxRoot))
            itr = itr + 1
        else:
            midTemp = midpoint
            ceiling = midpoint
            float(nextMidpoint = (ceiling + floor)/2)
            sqNextMidpoint = math.pow(nextMidpoint, 2)
            midpoint = nextMidpoint
            sqMidpoint = sqNextMidpoint
            aprxRoot = midpoint
            midDistance = midDistance
            f.write(str(n), str(itr), str(floor), str(ceiling), str(midpoint), str(sqMidpoint), str(midDistance), str(tolerance), str(aprxRoot))
            itr = itr + 1

    return aprxRoot



#   print final values
print "n is still n"
print "itr = " + str(itr)
print "floor = " + str(floor)
print "ceiling = " + str(ceiling)
print "midpoint = " + str(midpoint)
print "sqMidpoint = " + str(sqMidpoint)
print "midDistance = " + str(midDistance)
print "tolerance is the same" 
print "aprxRoot = " + str(aprxRoot)






