# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 03:31:57 2021

@author: vital
"""

import math
import matplotlib.pyplot as plt

def utility(beta0, beta1, beta2, beta3, beta4, Cmode, Cothermode, Tmode, Tothermode, Income, Numberofpeople):
    """Function calculates the utility of a transport mode.
    
    This function uses the following formula to calculate the utility of a
    transport mode using arguments that are described after the formula:
        Utility = beta0 + beta1*(Cmode - Cothermode) - beta2*(Tmode-Tothermode)
        + beta3*Income + beta4*Numberofpeople.
    
    Args:
        beta0: General calibration constant, depicting any other effects on
            utility except for Traveling Cost, Traveling Time, Household Income
            and Household Number of People. Derived theoretically during data
            preparation, fine-tuned during calibration.
        beta1: Calibration coefficient for the Traveling Cost parameters.
            Derived theoretically during data preparation, fine-tuned during
            calibration.
        beta2: Calibration coefficient for the Traveling Time parameters.
            Derived theoretically during data preparation, fine-tuned during
            calibration.
        beta3: Calibration coefficient for the Household Income parameter.
            Derived theoretically during data preparation, fine-tuned during
            calibration.
        beta4: Calibration coefficient for the Household Number of People
            parameter. Derived theoretically during data preparation,
            fine-tuned during calibration.
        Cmode: Traveling Cost of the first compared transport mode.
        Cothermode: Traveling Cost of the second compared transport mode.
        Tmode: Traveling Time of the first compared transport mode.
        Tothermode: Traveling Time of the second compared transport mode.
        Income: Household Income of the modeled household.
        Numberofpeople: Household Number of People of the modeled household.
    
    Returns:
        Utility: The utility of a transport mode.
    """
    Utility = beta0 + beta1*(Cmode - Cothermode) - beta2*(Tmode-Tothermode) + beta3*Income + beta4*Numberofpeople
    return Utility

def probability(util):
    """Function calculates mode choice probability based on its utility.
    
    This function uses the following formula to calculate the probability of
    travellers choosing a transport mode using arguments that are described
    after the formula:
        Probability = exp(Utility)/(1 + exp(Utility)).
    
    Args:
        util: Utility of a transport mode for travellers.
    
    Returns:
        Probability: Probability of travellers choosing a transport mode.
    """
    Probability = math.exp(util)/(1 + math.exp(util))
    return Probability

Income = 1
Numberofpeople = 1

beta0A = 1
beta1A = 1
beta2A = 1
beta3A = 1
beta4A = 1

CostA = 10
TimeA = 3

beta0T = 0.5
beta1T = 1
beta2T = 1
beta3T = 2
beta4T = 0.5

CostT = 5
TimeT = 5
    
UtilityA = utility(beta0A, beta1A, beta2A, beta3A, beta4A, CostA, CostT, TimeA, TimeT, Income, Numberofpeople)
UtilityT = utility(beta0T, beta1T, beta2T, beta3T, beta4T, CostT, CostA, TimeT, TimeA, Income, Numberofpeople)

ProbabilityA = probability(UtilityA)
ProbabilityT = probability(UtilityT)


choose_test = int(input('Input 1 for comparison by Time in Automobile mode and 2 for comparison by Cost in Transit mode? [1/2]'))

if choose_test == 1:
    list1 = []
    list1t = []
    for TimeA in range(2,20):
        list1.append(probability(utility(beta0A, beta1A, beta2A, beta3A, beta4A, CostA, CostT, TimeA, TimeT, Income, Numberofpeople)))
        list1t.append(TimeA)
    
    plt.plot(list1t, list1)
    plt.show()

if choose_test == 2:
    list2 = []
    list2t = []
    for CostT in range(5,1,-1):
        list2.append(probability(utility(beta0T, beta1T, beta2T, beta3T, beta4T, CostT, CostA, TimeT, TimeA, Income, Numberofpeople)))
        list2t.append(CostT)
    
    plt.plot(list2, list2t)
    plt.show()


