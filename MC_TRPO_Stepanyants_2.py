# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 03:31:57 2021

@author: vital
"""

import math
import matplotlib.pyplot as plt

### Trip Generation ##########################################################

"""
    4 Origins
    Number of trips (production & attraction for each Origin)
"""

TripGen = [[6900,7500],
           [8,11],
           [100,100],
           [830,790]]

### Trip Distribution ########################################################

"""
    Distance between origins:
"""

TimeAuto = [[1,8,5,7],
        [8,1,6,3],
        [5,6,1,1],
        [7,3,1,1]]
TimePublic = [[1,12,7,9],
        [12,1,5,4],
        [7,5,1,1],
        [9,4,1,1]]

maxTimeAuto = max(max(TimeAuto))
minTimeAuto = min(min(TimeAuto))
maxTimePublic = max(max(TimePublic))
minTimePublic = min(min(TimePublic))

CostAuto = [[2,5,3,4],
        [5,2,3,3],
        [3,3,2,2],
        [4,3,2,2]]
CostPublic = [[1,3,2,2],
        [3,1,2,2],
        [2,2,1,1],
        [2,2,1,1]]

maxCostAuto = max(max(CostAuto))
minCostAuto = min(min(CostAuto))
maxCostPublic = max(max(CostPublic))
minCostPublic = min(min(CostPublic))

"""
    Calculating a gravity coefficient for every origin combination =>
    => get the number of trips happening between every origin combination
"""

def gravityCoef(prod1, attr1, prod2, attr2, distance):
    tripnum = abs((attr1-prod1)*(attr2-prod2)/distance)
    return tripnum

TripDistributionTimeAuto = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
TripDistributionTimePublic = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
TripDistributionCostAuto = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
TripDistributionCostPublic = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for i in range (4):
    for j in range (4):
        TripDistributionTimeAuto[i][j] = gravityCoef(TripGen[i][1], TripGen[i][0], TripGen[j][1], TripGen[j][0], TimeAuto[i][j])

print("Trip Distribution depending on time for automobiles (number of trips betwee every origin combination):")
print(TripDistributionTimeAuto)
print()

for i in range (4):
    for j in range (4):
        TripDistributionTimePublic[i][j] = gravityCoef(TripGen[i][1], TripGen[i][0], TripGen[j][1], TripGen[j][0], TimePublic[i][j])

print("Trip Distribution depending on time for public (number of trips betwee every origin combination):")
print(TripDistributionTimePublic)
print()

for i in range (4):
    for j in range (4):
        TripDistributionCostAuto[i][j] = gravityCoef(TripGen[i][1], TripGen[i][0], TripGen[j][1], TripGen[j][0], CostAuto[i][j])

print("Trip Distribution depending on cost for automobiles (number of trips betwee every origin combination):")
print(TripDistributionCostAuto)
print()

for i in range (4):
    for j in range (4):
        TripDistributionCostPublic[i][j] = gravityCoef(TripGen[i][1], TripGen[i][0], TripGen[j][1], TripGen[j][0], CostPublic[i][j])

print("Trip Distribution depending on cost for public (number of trips betwee every origin combination):")
print(TripDistributionCostPublic)
print()

### Modal Choice #############################################################

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
    util_exp = math.exp(util)
    Probability = util_exp/(1 + util_exp)
    return Probability

"""
    Set the constant parameters for utility formula
"""

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

#choose_test = int(input('Input 1 for comparison by Time in Automobile mode and 2 for comparison by Cost in Transit mode? [1/2]'))

list1 = []
list1t = []
list2 = []
list2t = []
list3 = []
list3t = []
list4 = []
list4t = []

ProbabilityTimeAuto = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
ProbabilityTimePublic = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
ProbabilityCostAuto = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
ProbabilityCostPublic = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

"""
def plot (PM, minp,maxp,iterr,listn1,listn2):
    for PM in range(minp,maxp,iterr):
        listn1.append(probability(utility(beta0A, beta1A, beta2A, beta3A, beta4A, CostA, CostT, TimeA, TimeT, Income, Numberofpeople)))
        listn2.append(PM)
    plt.plot(listn2, listn1)
    plt.show()
        
plot(TimeA,minTimeAuto,maxTimeAuto,1,list1,list1t)
"""

print("max & min time auto:")
print(maxTimeAuto)
print(minTimeAuto)

#if choose_test == 1:
for TimeA in range(minTimeAuto,maxTimeAuto,1):
    list1.append(probability(utility(beta0A, beta1A, beta2A, beta3A, beta4A, CostA, CostT, TimeA, TimeT, Income, Numberofpeople)))
    list1t.append(TimeA)
plt.plot(list1t, list1)
plt.show()

for i in range (4):
    for j in range (4):
        ProbabilityTimeAuto[i][j] = probability(utility(beta0A, beta1A, beta2A, beta3A, beta4A, CostA, CostT, TimeAuto[i][j], TimeT, Income, Numberofpeople))

print("Probability depending on time for automobiles (number of trips betwee every origin combination):")
print(ProbabilityTimeAuto)
print()

#CostA = 10
TimeA = 3
#CostT = 5
#TimeT = 5

##############################################################################

print("max & min cost auto:")
print(maxCostAuto)
print(minCostAuto)

for CostA in range(maxCostAuto,minCostAuto,-1):
    list2.append(probability(utility(beta0A, beta1A, beta2A, beta3A, beta4A, CostT, CostA, TimeT, TimeA, Income, Numberofpeople)))
    list2t.append(CostA)
plt.plot(list2t, list2)
plt.show()

for i in range (4):
    for j in range (4):
        ProbabilityCostAuto[i][j] = probability(utility(beta0A, beta1A, beta2A, beta3A, beta4A, CostAuto[i][j], CostT, TimeA, TimeT, Income, Numberofpeople))

print("Probability depending on cost for automobiles (number of trips betwee every origin combination):")
print(ProbabilityCostAuto)
print()

CostA = 10
#TimeA = 3
#CostT = 5
#imeT = 5

##############################################################################

print("max & min time public:")
print(maxTimePublic)
print(minTimePublic)

#if choose_test == 2:
for TimeT in range(minTimePublic,maxTimePublic,1):
    list3.append(probability(utility(beta0T, beta1T, beta2T, beta3T, beta4T, CostT, CostA, TimeT, TimeA, Income, Numberofpeople)))
    list3t.append(TimeT)
plt.plot(list3t, list3)
plt.show()

for i in range (4):
    for j in range (4):
        ProbabilityTimePublic[i][j] = probability(utility(beta0T, beta1T, beta2T, beta3T, beta4T, CostA, CostT, TimeA, TimePublic[i][j], Income, Numberofpeople))

print("Probability depending on time for public (number of trips betwee every origin combination):")
print(ProbabilityTimePublic)
print()

CostA = 10
TimeA = 3
CostT = 5
TimeT = 5

##############################################################################

print("max & min cost public:")
print(maxCostPublic)
print(minCostPublic)

for CostT in range(maxCostPublic,minCostPublic,-1):
    list4.append(probability(utility(beta0T, beta1T, beta2T, beta3T, beta4T, CostT, CostA, TimeT, TimeA, Income, Numberofpeople)))
    list4t.append(CostT)
plt.plot(list4t, list4)
plt.show()

for i in range (4):
    for j in range (4):
        ProbabilityCostPublic[i][j] = probability(utility(beta0T, beta1T, beta2T, beta3T, beta4T, CostA, CostPublic[i][j], TimeA, TimeT, Income, Numberofpeople))

print("Probability depending on cost for public (number of trips betwee every origin combination):")
print(ProbabilityCostPublic)
print()

### Mode Share Percentages ###################################################
    
ProbTimeAuto = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
ProbTimePublic = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
ProbCostAuto = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
ProbCostPublic = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

TripDist = 0
Pr = 0
"""
TripDistTimePublic = 0
PrTimePublic = 0
TripDistCostAuto = 0
PrCostAuto = 0
TripDistCostPublic = 0
PrCostPublic = 0
"""

for i in range (4):
    for j in range (4):
        ProbTimeAuto[i][j] = TripDistributionTimeAuto[i][j] * ProbabilityTimeAuto[i][j]
for i in range (4):
    for j in range (4):
        TripDist += TripDistributionTimeAuto[i][j]
for i in range (4):
    for j in range (4):
        Pr += ProbTimeAuto[i][j]
        
for i in range (4):
    for j in range (4):
        ProbTimePublic[i][j] = TripDistributionTimePublic[i][j] * ProbabilityTimePublic[i][j]
for i in range (4):
    for j in range (4):
        TripDist += TripDistributionTimePublic[i][j]
for i in range (4):
    for j in range (4):
        Pr += ProbTimePublic[i][j]

for i in range (4):
    for j in range (4):
        ProbCostAuto[i][j] = TripDistributionCostAuto[i][j] * ProbabilityCostAuto[i][j]
for i in range (4):
    for j in range (4):
        TripDist += TripDistributionCostAuto[i][j]
for i in range (4):
    for j in range (4):
        Pr += ProbCostAuto[i][j]

for i in range (4):
    for j in range (4):
        ProbCostPublic[i][j] = TripDistributionCostPublic[i][j] * ProbabilityCostPublic[i][j]
for i in range (4):
    for j in range (4):
        TripDist += TripDistributionCostPublic[i][j]
for i in range (4):
    for j in range (4):
        Pr += ProbCostPublic[i][j]        

probmodechoiceauto = Pr/TripDist
print("Probability of chosing an automobile for a trip:")
print(probmodechoiceauto)