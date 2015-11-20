"""
Author: Mike Remondi
Date: November 20, 2015

This program models implements functions that model the single, continuous variable
uniform, normal, gamma, and beta distributions
"""

import matplotlib, matplotlib.pyplot
import numpy
import math

# Draws a uniform distribution and returns the expected value and variance
def uniform(a, b):
    a = float(a)
    b = float(b)
    
    # Creates a list of 500 x values ranging from a to b
    x_data = numpy.linspace(a,b,500)
    
    # Computes a y value for every x value and plots each (x,y)
    for x in x_data:
        y = 1/(b-a)
        matplotlib.pyplot.plot(float(x),float(y), 'k_')
        
    # Axes formatting
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel("y")
    axes.set_ylabel("f(y)")
    matplotlib.pyplot.show()
    
    # calculates the expected value and variance
    e = (a + b)/2
    v = ((b - a)**2)/12
    
    return e, v, "uniform distribution"
    
# Draws a normal distribution and returns the expected value and variance
def normal(mean, variance):
    mean = float(mean)
    variance = float(variance)
    
    # Standard deviation
    sigma = math.sqrt(variance)

    # Creates a list of 500 x values ranging from +- 3 standard deviations from the mean
    x_data = numpy.linspace(mean-3*sigma, mean+3*sigma, 500)
    
    # Computes a y value for every x value and plots each (x,y)
    for x in x_data:
        factor1 = 1/(sigma*2*math.pi)
        factor2 = math.e
        exponent = -((x-mean)**2)/(2*variance)
        y = (factor1 * math.pow(factor2, exponent))
        matplotlib.pyplot.plot(float(x), float(y),'k.')
        
    # Axes formatting
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel("y")
    axes.set_ylabel("f(y)")
    matplotlib.pyplot.show()
    
    # expected value and variance
    e = mean
    v = variance 
    
    return e, v, "normal distribution"
    
# Recursive function that returns the factorial of n-1
def gamma_func(n):
    if (n<=1):
        return 1
    else:
        return float(n*gamma_func(n-1))

# Draws a gamma distribution and returns the expected value, variance
# and returns the type of distribution if it is either an exponential or 
# chi-square distribution
#
# Note: Only plots from 0 to 20 on the x axis.
def gamma(alpha, beta):
    alpha = float(alpha)
    beta = float(beta)
    
    # Creates a list of 500 x values ranging from 0 to 20
    x_data = numpy.linspace(0, 20, 500)
    
    # Computes a y value for every x value and plots each (x,y)
    for x in x_data:
        numerator = float(math.pow(x, alpha-1) * math.pow(math.e, -x/beta))
        denominator = float(math.pow(beta, alpha) * gamma_func(alpha))
        y = float(numerator/denominator)
        matplotlib.pyplot.plot(float(x), float(y),'k.')
        
    # Axes formatting
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel("y")
    axes.set_ylabel("f(y)")
    matplotlib.pyplot.show()
    
    # if beta is 2 then it is a chi-square distribution
    if (beta == 2):
        
        # calculates the expected value and variance
        e = alpha * 2
        v = e * 2
        description = "chi-square with " + str(e) + " degrees of freedom"
        
        return e, v, description
    
    # if alpha is 1 and beta is greater than 0 it is an exponential distribution
    elif (alpha==1 and beta > 0):
        
        #calculates the expected value and variance
        e = beta
        v = beta**2
        
        return e, v, "expontential distribution"
    
    # else it is a normal gamma distribution
    else:
        # calculates the expected value and variance
        e = alpha*beta
        v = alpha*(beta**2)
    
        return e, v, "gamma distribution"

# Takes two parameters and uses the gamma_func recursive function and returns a value
def beta_func(alpha, beta):
    return float(gamma_func(alpha)*gamma_func(beta)/gamma_func(alpha+beta))
    
# Draws a normal distribution and returns the expected value and variance
#
# Note: Currently only works for alpha >= 1 and beta >= 1
def beta(alpha, beta):
    alpha = float(alpha)
    beta = float(beta)
    
    # Creates a list of 500 x values ranging from 0 to 1
    x_data = numpy.linspace(0, 1, 500)
    
    # Computes a y value for every x value and plots each (x,y)
    for x in x_data:
        numerator = float(math.pow(x,alpha-1)*math.pow(1-x,beta-1))
        denominator = float(beta_func(alpha, beta))
        y = float(numerator/denominator)
        matplotlib.pyplot.plot(float(x), float(y),'k.')
    
    # Axes formatting
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel("y")
    axes.set_ylabel("f(y)")
    matplotlib.pyplot.show()
    
    # Calculates the expected value and variance
    e = alpha/(alpha + beta)
    v = (alpha*beta)/((alpha+beta)**2)*(alpha+beta+1)
    
    return e, v, "beta distribution"
    
def main():
    print uniform(10,20)
    print normal(10, 5)
    print gamma(5,5)
    print gamma(1, 10)
    print gamma(5, 2)
    print beta(3, 1)
    
if __name__ == "__main__":
    main()