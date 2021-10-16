# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 03:31:57 2021

@author: vital
"""

import math
import matplotlib.pyplot as plt

def utility(beta0, beta1, beta2, beta3, beta4, Cmode, Cothermode, Tmode, Tothermode, Income, Numberofpeople):
    Utility = beta0 + beta1*(Cmode - Cothermode) - beta2*(Tmode-Tothermode) + beta3*Income + beta4*Numberofpeople
    return Utility

def probability(util):
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

list1 = []
list1t = []
for TimeA in range(2,20):
  list1.append(probability(utility(beta0A, beta1A, beta2A, beta3A, beta4A, CostA, CostT, TimeA, TimeT, Income, Numberofpeople)))
  list1t.append(TimeA)

plt.plot(list1t, list1)
plt.show()

list2 = []
list2t = []
for CostT in range(5,1,-1):
  list2.append(probability(utility(beta0T, beta1T, beta2T, beta3T, beta4T, CostT, CostA, TimeT, TimeA, Income, Numberofpeople)))
  list2t.append(CostT)

plt.plot(list2, list2t)
plt.show()