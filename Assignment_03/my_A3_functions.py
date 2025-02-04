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
    # None
    CESutility_valid(5, -8, 3)
    # None
    CESutility_valid(5, 8, -3)
    # None
