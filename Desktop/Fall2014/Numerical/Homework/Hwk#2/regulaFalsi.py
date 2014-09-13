#! /usr/bin/env python 

#   Kristi Short
#   Numerical Analysis 
#   Math151
#   Fall 2014
#   Hwk#2: Illinois Algorithm 

#   Let h(x) = cos(x) - x^3 = 0, for x element of the Reals.
#   Then let f(x) = cos(x) 
#   And g(x) = x^3
#   We want to find where f(x) = g(x).
#   i.e. Where h(x) has a zero. 


import math


#   Vars
itr = 0
a = (-.5)       # x_0
b = 1           # x_1
x = 0
end = 30


#   h(x) is an odd function, so it has only one root at x = 0.86547403310161444662

def f(x):
    return math.cos(x) - x**3 

def see(a,b):
    c = (a*f(b) - b*f(a))/(f(b) - f(a))
    return c


p = see(a,b)

def replace(a, b, p):
    if (f(a)*p > 0):
        b = see(a,b)
        return b
    else:
        a = see(a,b)
        return a


#   ************ Get(ROOT) ************************************************

while (itr < end):
    if (f(a)*f(b) < 0):
        itr = itr + 1
        newEnd = replace(a, b, p)
    else:
        itr - itr + 1
        c = (.5*f(b)*a - f(a)*b)/(.5*f(b) - f(a))
        if (f(a)*f(b) < 0):
            newEnd = replace(a, b, p)
        else:
            itr = itr + 1
            c = (f(b)*a - .5*f(a)*b)/(f(b) - .5*f(a))
            newEnd = replace(a, b, p)
            
print "x = " + str(c)




#   **********************************************************************



