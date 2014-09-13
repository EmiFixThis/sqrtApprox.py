#	Kristi Short
#	Math 180 Numerical Analysis
#	Fall 2014
#	Square Root Approximation
#	Pythonista Version

import math

#	prompt user for radicand
n = float(raw_input("Please enter an integer value for the radicand: "))
toleranceVal = float(raw_input("Please enter a positive integer value for the power of the tolerance: "))
tolerance = math.pow(10, -toleranceVal)
sqRt = math.sqrt(n)
err = 0
print "Note: Computer memory is system dependent, floats are limited in accuracy. So unless you are running something seriously badass dont ask for a tolerance value larger than 6 or so."

def findRoot(n, tolerance):
	itr = 0
	with open('SquareRootAprxData', 'w') as f:
		f.write('#itr,floor, celing, prevMid, mid\n')
		sqRt = math.sqrt(n)
		floor = 0
		ceiling = n
		mid = n
		prevMid = -1
		err = 0
		while (math.fabs(mid - prevMid) >= tolerance):
			f.write('{0},{1},{2},{3}\n'.format(itr,floor,ceiling,prevMid,mid))
			prevMid = mid
			mid = float((floor+ceiling)/2)
			if mid**2 > n:
				ceiling = mid
			else: 
				floor = mid
			itr = itr + 1
		return mid
		
root = findRoot(n, tolerance)
err = math.fabs(root - sqRt)
print "The approximated root of " + str(n) + " is " + str(root)
print "The error in Approximation is: " + str(err)
