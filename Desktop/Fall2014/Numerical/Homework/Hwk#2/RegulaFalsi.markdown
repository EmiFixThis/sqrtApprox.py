Title: RegulaFalsi
Timestamp: 2014-09-08 10:07:38 +0000
Created: 2014-09-05 15:54:21 +0000
Last Accessed: 2014-09-05 15:54:21 +0000
Times Accessed: 0
Tags: 
Metadata: 
# Regula Falsi (Method of False Position) #


>	False position problems are more or less "*guess and check*" problems. <br />
>	The method involves attempting to solve the problem using test values (that may be false), and then adjusting the values as needed. <br />

>	Simple False Position
>	:	Solves problems that can be phrased in terms of direct proportionality. 
>	:	i.e. Find *x* for *ax* = *b*. 

>	Double False Position 
>	:	Solves more complicated problems that can be written functionally, when given two solutions (or possible solutions). 
>	:	The double false position method is equivalent to linear interpolation and provides an exact solution, when *f* is an affine linear function (*f*(*x*) = *ax* + *c*, for some constant *c*). 
>	:	If *f* is not linear then the method gives an approximation that improves under iteration. 

>	**Regula Falsi:**
>	As an algorithm refers to a method of finding polynomial roots, which is more or less a hybrid method that utilizes concepts from both the secant method and the bisection method for finding polynomial roots. 
>	This root finding method is called the *double false position* method, as you begin by choosing two numbers *a_0* and *b_0* such that *f*(*a_0*) and *f*(*b_0*) are opposite in sign (invoke IVT). 
>	i.e. The problem can be phrased in the form determine x for *f*(*x*) = *b*, if we already know that *f*(*x_1*) = *b_1* and *f*(*x_2*) = *b_2*. 

## Assumptions, Conditions, and Comparison to Other Methods ##

>	**Bisection Method (Binary Search Algorithm)**
>	:	Assume *f*(*x*) is continuous on an interval [*a*, *b*], and that *f*(*a*) and *f*(*b*) have opposite signs. 

>	**Basic Method:** 
>	:	Find the midpoint of the interval, *c*.
>	:	Calculate the value of *f*(*c*). 
>	:	Check if the convergence is in the range of the tolerance. i.e. Check (*a* - *c*) or *f*(*c*) is ≤ tolerance value. 
>	:	If *f*(*c*) converges within tolerance then stop iteration and return *c*.
>	:	Else, check the sign of *f*(*c*) and replace either (*a*, *f*(*a*)) or (*b*, *f*(*b*)), depending on the sign. 
>	:	The bisection method only relies on the continuity of *f* to determine the root.  

>	The bisection method is pretty slow, and only gives one bit of increased accuracy per iteration. Requires that *f* be continuous and apriori knowledge of two initial values *a* and *b* having opposite signs. However, it is simple, and computationally inexpensive. 

>	**Secant Method:**
>	The secant method has the condition that *a* and *b* be chosen so that they are close to the root. The secant method does not require that *a* and *b* have opposite signs.
>	That the secant method does not invoke IVT means, the secant method may not converge at all if it does not meet the additional constraints that *f* be twice continuous differentiable, and the root have a singular multiplicity. 
>	In effect, the secant method replaces the derivative with an approximation. 

>	**Regula Falsi:**
>	As with the bisection method regula falsi requires that *f*(*a*) and *f*(*b*) have opposite signs. 
>	As with the bisection method we adjust the range after each iteration to ensure that the root remains within the interval we manipulate. This ensures that as the iteration progresses we receive a set of intervals that reduce in size and all contain the root. 
>	The adjustment of the interval in this way ensure that the regula falsi method always converges. 
>	The difference between the bisection method and the regula falsi method is simply that bisection uses:
>	*c_k* = (*a_k* + *b_k*)/2
>	While regula uses:
>	*c_k* = *b_k* - (*f*(*b_k*)(*b_k* - *a_k*))/(*f*(*b_k*) - *f*(*a_k*))

>	
>	**Basically regula falsi keeps the interval where you want it.** 
>	i.e. Exactly in an interval where the root always exists. <br />

>	**Failures:**
>	1.	Regula falsi may fail if the second derivative of *f* is constant on [*a*, *b*]. If this occurs then one of the endpoints will not get closer to the root as iteration progresses and will stay fixed. i.e. The bracket interval will not converge to zero. 
>	2.	If *f* is discontinuous regula will only find the root at a point where *f* changes in sign. It may also happen that *f* may converge to zero at a point where *f* does not exist. Bisection avoids this problem. 
>	These two failures may be avoided by adjusting regula so that the next position is modified either:
>	*c_k* = (.5*f*(*b_k*)*a_k* - *f*(*a_k*)*b_k*)/(.5*f*(*b_k*) - *f*(*a_k*))
>	or
>	*c_k* = (*f*(*b_k*)*a_k* - .5*f*(*a_k*)*b_k*)/(*f*( *b_k*) - .5*f*(*a_k*)).
>	This modification is called the Illinois algorithm. 



## Algorithm ##

>	Assume f(x) is continuous on some interval [a,b] such that a and b are chosen so 
>	that f(a) is opposite in sign from f(b)
>	i.e. (f(a))(f(b)) < 0
			
			itr = itr + 1
			a = (-0.5)
			b = 1
			c = 0
			x = 0
			f = math.cos(x)
			g = x**3
			


			def f(x):
				return math.cos(x) - x**3


			def see(a, b):
				c = ((f(b)(b - a))/(f(b) - f(a)))
				return c

			
			def replace(a, b, f(c)):
				if (f(a)*f(c) > 0):
					b = c
					return b
				else:
					a = c
					return a


#	****************************************** Get(root) ********************************************************************************

while (x != 0.86547403310161444662):

	if (f(a)*f(b) < 0):
		itr++
		replace(a, b, f(c)):
		f(a);
		f(b);
		see(a, b);
		print "x = " + str(c)
	else:
		itr++
		c = (.5*f(b))*a - f(a)*b)/(.5*f(b) - f(a))
		replace(a, b, f(c));
		if (f(a)*f(b) < 0):
			f(a);
			f(b);
			

		



