# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 3311: Python for Business Analytics
# Assignment_04
#
# Drew Cragin
# Heriberto Elizarraras
# University of Central Florida
#
# February 17, 2025
#
##################################################
"""
import numpy as np

def matrix_inverse(mat_in): # expected input/output? (-2)
    """ Calculates the inverse of the two-by-two matrix mat_in
    using the formula for the inverse of a two-by-two matrix
     ( 1 / a11*a22 - a12*a21 ) * the matrix
     
    >>> matrix_inverse(np.array([[4, 9], [1, 4]]))
    [[ 0.57142857 -1.28571429]
     [-0.14285714  0.57142857]]
        
    """
    
    # Incorrect test cases (-2)
    
    if mat_in.shape != (2,2):
        print("Warning: Shape must be 2x2.")
        return None
    
    a11 = mat_in[0, 0]
    a12 = mat_in[0, 1]
    a21 = mat_in[1, 0]
    a22 = mat_in[1, 1]
    
    dterm=(a11 * a22) - (a12 * a21)
    
    if dterm == 0:
        print("Warning: Matrix is singular")
        return None

    mat_out=np.zeros((2,2))
    mat_flip=np.array([[a22,-a12],[-a21,a11]])
    
    for row in range(2):
        for column in range(2):
            mat_out[row,column]=(1/dterm)*mat_flip[row,column] # not the proper steps, supposed to utilize the loops to avoid lines 35-38 (-2)
    
    return mat_out

def logit_like_sum(y: list, x: list, beta0: float, beta1: float) -> float:
    """ Calculates the sum of the log-likelihood across all observations,
    first calculating the logit function, calculating the log-likelihood,
    and then summing the log-likelihoods.
    
    y - Numpy array or list determing binary result
    x - Numpy array or list independent variable
    beta0 - The intercept coefficient
    beta1 - The slope coefficient
    
    >>> logit_like_sum([4, 2, 5], [3, 1, 6], 0.2, 1.5)
    52.42305877214691
    >>> logit_like_sum([3, 2, 8], [7, 7, 4], 0.1, 0.5)
    25.33056629080383
    >>> logit_like_sum([8, 8, 1], [9, 4, 1], 2.5, 2.1)    
    226.0899802301752
    """
    
    # failed to check if y len = x len (-1)
    y = np.array(y)
    x = np.array(x)
    
    logit = np.exp(beta0 + x * beta1) / (1 + np.exp(beta0 + x * beta1))
    
    log_likelihood = y * np.log(logit) + (1 - y) * np.log(1 - logit) # Clever, but what if y does not equal 0 or 1? (-1)
    
    total_log_likelihood = np.sum(log_likelihood)

    return total_log_likelihood  


def logit_like_grad(y: list, x: list, beta0: float, beta1: float) -> float:
    """Calculates the gradient vector of the likelihood function
    for the bivariate logistic regression model
    for sevaral pairs of observations in the lists x and y,
    coefficients beta_0 and beta_1.
    
    y - Numpy array or list determing binary result
    x - Numpy array or list independent variable
    beta0 - The intercept coefficient
    beta1 - The slope coefficient

    >>> logit_like_grad([1, 1, 0, 0], [15.0, 5.0, 15.0, 5.0], 0.0, 0.0)
    [0.0, 0.0]
    >>> logit_like_grad([1, 1, 0, 0], [15.0, 5.0, 15.0, 5.0], math.log(3), 0.0)
    [-1.0, -10.0]
    >>> logit_like_grad([1, 1, 0, 0], [15.0, 5.0, 15.0, 5.0], math.log(7), 0.0)
    [-1.5, -15.0]
    >>> logit_like_grad([1, 0, 1], [1, 1, 1], 0.0, math.log(2))
    [0.0, 0.0]
    >>> logit_like_grad([1, 0, 1], [1, 1, 1], 0.0, math.log(5))
    [-0.5, -0.5]
    >>> logit_like_grad([1, 0, 1], [3, 3, 3], 0.0, math.log(2))
    [-2/3, -2.0]
    """
    gradient_b0 = 0
    gradient_b1 = 0
    
    # failed to check if y len = x len (-1)
    
    for i in range(len(y)):
        log_function = 1 / (1 + np.exp(-(beta0 + beta1 * x[i])))
        
        if y[i] == 1:
            gradient_b0 += 1 - log_function
            gradient_b1 += x[i] * (1 - log_function)
        elif y[i] == 0:
            gradient_b0 += -log_function
            gradient_b1 += x[i] * (-log_function)
        else:
            print("Error")
            return None
        
    return np.array([gradient_b0, gradient_b1])

def CESutility_multi(x: list, a: list, r: float) -> float:
   """Calculates the consumer utility for more than two goods
   
   x - Vector of quantities
   a - Vector of weighting parameters for each good
   r - Elasticity parameter
   
   >>> CESutility_multi([3, 4, 5], [1, 5, 2], 1.5)
   6.528142797805768
   >>> CESutility_multi([3, -4, 5], [1, 5, 2], 1.5)
   Error: Values must be positive
   >>> CESutility_multi([3, 4, 5, 6], [1, 5, 2], 1.5)
   Error: Lengths must be equal
   """
   if any(val < 0 for val in x) or any(val < 0 for val in a):
       print("Error: Values must be positive")
       return None
    
   if len(x) != len(a):
       print("Error: Lengths must be equal")
       return None
   
# What about r? (-1)
   
   if len(x) == len(a):
       utility = sum(a[i]**(1-r) * x[i]**r for i in range(len(x))) ** (1/r)
       return utility
   
   else:
       return None

# No Doctest and no output file (-7)