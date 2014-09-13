#! usr/bin/env python

#   Regula Falsi with Illinois Modification

import math

#   Ends
a = (-0.25)
b = 1

maxItr = 30
x = 0
xAB = 0

def f(x):
    return math.cos(x) - x**3

fa = f(a)
fb = f(b)

def root(a, b, fa, fb):
    x = a - fa*((b-a)/(fb - fa))
    return x

fx = f(x)

def regF(a, b, fa, fx):
#    x = root(a,b,fa,fb)
    itr = 0
    maxItr = 30
    while (itr < maxItr):
        fx = root(a, b, fa, fb)
        if fa*fx < 0:
            b = fx
        else:
            a = fx
        itr = itr + 1
    return fx

print "Value of the root is: " + str(fx)



