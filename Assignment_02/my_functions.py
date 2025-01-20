# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 3311: Python for Business Analytics
# Assignment_02
#
# Drew Cragin
# University of Central Florida
#
# January 20, 2025
#
##################################################
"""
def present_value(cash_flow_amt, discount_rate: float, num_years) -> float:
    """ Calculates the present value of a future cash flow
    Using the present value formula PV = FV / (1+r)^n
    
    cash_flow_amt - Future Value of money
    discount_rate - Interest or discount rate in decimal form
    num_years - number of years cash flow is to be recieved in the future
    
    >>> present_value(10,.03,6)
    8.37
    >>> present_value(150,.09, 12)
    53.33
    """
    
    total = cash_flow_amt / ((1 + discount_rate) ** num_years)
    
    return total

# Testing the function
present_value(10,.03,6)
# 8.37
present_value(150,.09, 12)
# 53.33

def future_value(cash_flow_amt, discount_rate: float, num_years) -> float:
    """ Calculates the future value of a present cash flow
    Using the future value formula FV = PV * (1+r)^n
    
    cash_flow_amt - Present Value of money
    discount_rate - Interest or discount rate in decimal form
    num_years - number of years cash flow is to be invested for the future
    
    >>> present_value(10,.03,6)
    11.94
    >>> present_value(150,.09, 12)
    53.33
    """
    
    total = cash_flow_amt * ((1 + discount_rate) ** num_years)
    
    return total

# Testing the function
future_value(10,.03,6)
# 11.94
future_value(150, .09, 12)
# 421.90

def total_revenue(num_units, price: float) -> float:
    """ Calculates the revenue earned by a firm selling a product at
    a fix price using the formula price * units sold
  
    >>> total_revenue(10,15.50)
    155.00
    >>> total_revenue(8, 5.25)
    42.00
    """
    total = num_units * price
    
    return total
    
# Testing the function
total_revenue(10,15.50)
# 155.0
total_revenue(8,5.25)
# 42.0

def total_cost(num_units, fixed_costs: float, cost_coeff: float) -> float:
    """ Calculates total cost incurred to produce a product using the 
    formula TC = a * quantity^2 + FC

    num_units - Number of units produced
    fixed_costs - total amount of fixed costs
    cost_coeff - constant that is multiplied by square of units produced

    >>> total_cost(400,4000.0,1.0)
    164,000.0
    >>> total_cost(50,1300.0,2.9)
    8550.0
    """
    total = cost_coeff * num_units**2 + fixed_costs
    
    return total

# Testing the function
total_cost(400,4000.0,1.0)
# 164,000.0
total_cost(50,1300.0,2.9)
# 8550.0
total_cost(130,12000.0,0.88)
# 26872.0

def CESutility(consumed_good1, consumed_good2, degree_complements: float) -> float:
    """ Calculates value of Constant Elasticity of Substitution utility function
    which measures degree of satisfaction a consumer gets from two goods with formula
   (x^r+y^r)^1/r

    consumed_good1 - Quantity of good 1 consumed
    consumed_good2 - Quantity of good 2 consumed
    degree_complements - Degree to which the goods are complements or substitutes

    >>> CESutility(40,55,0.7)
    127.38
    >>> CESutility(170,168,-0.35)
    23.323
    """
    total = round((consumed_good1 ** degree_complements + consumed_good2 ** degree_complements)**(1/degree_complements),3)
    
    return total

# Testing the function
CESutility(40,55,0.7)
# 127.38
CESutility(170,168,-0.35)
# 23.323
CESutility(1030,1600,0.9)
# 2833.825
