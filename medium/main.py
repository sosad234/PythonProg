from bank_services import calculate_credit, calculate_installment, calculate_deposit

def run_app(service, amount, rate, term):
    if service == 'Кредит':
        result = calculate_credit(float(amount), float(rate), int(term))
    elif service == 'Рассрочка':
        result = calculate_installment(float(amount), float(rate), int(term))
    elif service == 'Вклад':
        result = calculate_deposit(float(amount), float(rate), int(term))
    return result

def save_to_doc(result):
    # Сохранение в DOC файл
    pass

def save_to_xls(result):
    # Сохранение в XLS файл
    pass

if __name__ == '__main__':
    # Здесь вызов функции, отвечающей за GUI
    pass
