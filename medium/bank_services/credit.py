def calculate_credit(amount, rate, term, payment_type='annuity'):
    monthly_rate = rate / 12 / 100
    
    if payment_type == 'annuity':
        annuity_coefficient = monthly_rate * (1 + monthly_rate) ** term / ((1 + monthly_rate) ** term - 1)
        monthly_payment = amount * annuity_coefficient
    elif payment_type == 'differentiated':
        monthly_payment = amount / term + (amount - (amount / term) * (term - 1)) * monthly_rate
    else:
        raise ValueError('Unknown payment type')
    
    return monthly_payment
