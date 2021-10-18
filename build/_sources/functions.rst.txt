MC_TRPO's documentation
=======================  


>>> def utility(beta0, beta1, beta2, beta3, beta4, Cmode, Cothermode, Tmode, Tothermode, Income, Numberofpeople):
...    Utility = beta0 + beta1*(Cmode - Cothermode) - beta2*(Tmode-Tothermode) + beta3*Income + beta4*Numberofpeople
...    return Utility

Function calculates the utility of a transport mode.
    
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


>>> def probability(util):
...    Probability = math.exp(util)/(1 + math.exp(util))
...    return Probability

Function calculates mode choice probability based on its utility.
    
    This function uses the following formula to calculate the probability of
    travellers choosing a transport mode using arguments that are described
    after the formula:
    Probability = exp(Utility)/(1 + exp(Utility)).
    
    Args:
        util: Utility of a transport mode for travellers.
    
    Returns:
        Probability: Probability of travellers choosing a transport mode.
