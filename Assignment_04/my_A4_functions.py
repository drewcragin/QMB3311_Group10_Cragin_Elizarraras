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

def matrix_inverse(mat_in):
    """ Calculates the inverse of the two-by-two matrix mat_in
    using the formula for the inverse of a two-by-two matrix
     ( 1 / a11*a22 - a12*a21 ) * the matrix
     
    Inverse matrix example
    >>> mat_in = np.array([[3, 8], [1, 4]])
        mat_out = matrix_inverse(mat_in)
        print(mat_out)
        [[ 0.57142857 -1.28571429]
         [-0.14285714  0.57142857]]
        
    mat_in.dot(mat_out) example
    >>> example1 = np.dot(mat_in, mat_out)
    print(example1
    [[1. 0.]
     [0. 1.]]
    
    mat_out.dot(mat_in) example
    >>> example2 = np.dot(mat_out, mat_in)
    print(example2)
    [[1. 0.]
     [0. 1.]]
    
    Return x and b example
    >>> b = np.array([[3], [6]])
    x = np.dot(mat_out, b)
    print (np.dot(mat_in, x))
    print (x)
    [[3.]
     [6.]]
    [[-6.]
     [ 3.]]
    """
    if mat_in.shape != (2,2):
        print("Warning: Input must be a 2x2 matrix.")
        return None
    
    a11 = mat_in[0, 0]
    a12 = mat_in[0, 1]
    a21 = mat_in[1, 0]
    a22 = mat_in[1, 1]
    
    det = a11 * a22 - a12 * a21
    
    if det == 0:
        print("Warning: Matrix is singular")
        return None
    
    inv_det = 1 / det
    mat_out = np.array([[a22, -a12], [-a21, a11]]) * inv_det
    
    return mat_out
    
# Inverse matrix test
mat_in = np.array([[4, 9], [1, 4]])
mat_out = matrix_inverse(mat_in)
print(mat_out)
# mat_in.dot(mat_out) test
example1 = np.dot(mat_in, mat_out)
print(example1)
# mat_out.dot(mat_in) test
example2 = np.dot(mat_out, mat_in)
print(example2)
# Return x and b test
b = np.array([[3], [6]])
x = np.dot(mat_out, b)
print (np.dot(mat_in, x))
print (x)
