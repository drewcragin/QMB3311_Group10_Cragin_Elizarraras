# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 3311: Python for Business Analytics
# Assignment_03
#
# Drew Cragin
# Heriberto Elizarraras
# University of Central Florida
#
# February 3, 2025
#
##################################################
"""
def CESutility_valid(consumed_good1, consumed_good2, degree_complements: float) -> float:
    """ Calculates value of Constant Elasticity of Substitution utility function
   which measures degree of satisfaction a consumer gets from two goods with formula
  (x^r+y^r)^1/r while 

   consumed_good1 - Quantity of good 1 consumed
   consumed_good2 - Quantity of good 2 consumed
   degree_complements - Degree to which the goods are complements or substitutes

   >>> CESutility_valid(5, 8, 3)
   8.604
   >>> CESutility_valid(-5, 8, 3)
   None
   >>> CESutility_valid(5, -8, 3)
   None
   >>> CESutility_valid(5, 8, -3)
   None
   """
    if consumed_good1 < 0:
        print("X Can not be a negative number")
        return None
    if consumed_good2 < 0:
        print ("Y can not be a negative number")
        return None
    if degree_complements <= 0:
        print ("r must be strictly positive")
        return None
    
    total = round((consumed_good1 ** degree_complements + consumed_good2 ** degree_complements)**(1/degree_complements),3)
   
    return total

    # Testing the function
    CESutility_valid(5, 8, 3)
    # 8.604
    CESutility_valid(-5, 8, 3)
    # Error message for x
    CESutility_valid(5, -8, 3)
    # Error message for y
    CESutility_valid(5, 8, -3)
    # Error message for r
    
    def CESutility_in_budget(consumed_good1, consumed_good2, degree_complements: float, p_x, p_y, w) -> float:
        """ Evaluates the CESutility_valid function when the consumer's choice of goods
        x and y are in budget, and returns None otherwise using the wealth formula
        w >= p_x*x + p_y*y
    
        consumed_good1 - Quantity of good one
        consumed_good2 - Quantity of good two
        r - Degree to which the goods are complements or substitutes
        p_x - Price of good one
        p_y - Price of good two
        w - Wealth
        
        >>> CESutility_in_budget(5, 3, 2, 2, 2, 20)
        5.831
        >>> CESutility_in_budget(5, 3, 2, 2, 2, 4)
        None
        >>> CESutility_in_budget(5, 3, -2, 2, 2, 20)
        None
        >>> CESutility_in_budget(5, 3, 2, -2, 2, 20)
        None
        """
        if p_x < 0:
            print("Price of X can not be negative")
            return None
        if p_y < 0:
            print("Price of Y can not be negative")
            return None
        
        if w < p_x*consumed_good1 + p_y*consumed_good2:
            print("Consumers basket of goods can not exceed wealth")
            return None
        
        return CESutility_valid(consumed_good1, consumed_good2, degree_complements)
        
        # Testing the function
        CESutility_in_budget(5, 3, 2, 2, 2, 20)
        # 5.831
        CESutility_in_budget(5, 3, 2, 2, 2, 4)
        # Error message for wealth
        CESutility_in_budget(5, 3, -2, 2, 2, 20)
        # Error message for r
        CESutility_in_budget(5, 3, 2, -2, 2, 20)
        # Error message for p_x

import math
def logit(x,beta0,beta1):
    """calculates the logit link function, which gives the probability of a binary result [prob(y=1|x)] in a form that can be 
    modelled linearly. e^b0+xb1 / 1+e^ b0+xb1

    x- independent input value
    beta0- parameter 1, commonly intercept
    beta1- parameter 2, commonly slope

    >>>logit(70,2,3)
    1
    >>>logit(1,0.5,1)
    0.8175744761936437
    >>>logit(-1,2,2)
    0.5
    """
    answer= math.exp((beta0 + x * beta1)) / (1 + math.exp(beta0 + x * beta1))
    return answer
