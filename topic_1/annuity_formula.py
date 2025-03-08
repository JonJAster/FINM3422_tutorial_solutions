## Answer for Tutorial 1

def annuity_formula_function(interest_rate: float, number_of_periods, payment_amount):
    """
    Calculate the Present Value (PV) of an annuity.

    Parameters:
    interest_rate (float): The interest rate per period (as a decimal, e.g., 5% = 0.05).
    number_of_periods (int): The total number of periods.
    payment_amount (float): The fixed payment per period.

    Returns:
    float: The present value of the annuity.
    """
    if interest_rate == 0: # Edge case when interest rates are 0
        return payment_amount * number_of_periods  
    
    return payment_amount * ((1 - (1 + interest_rate)** (-number_of_periods)) / interest_rate)