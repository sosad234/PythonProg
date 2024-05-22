def calculate_deposit(amount, rate, term):
    # здесь реализация расчета вклада
    # предположим, что капитализация процентов происходит ежемесячно
    total_amount = amount
    for i in range(term):
        total_amount += total_amount * (rate / 100 / 12)
    return total_amount
