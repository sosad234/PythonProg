# Кредит 


import math

def calculate_percent(principal, rate, periods): # Метод прямоугольников
    integral = 0
    width = 1 / periods

    for i in range(periods):
        x = (i + 0.5) * width
        height = principal * rate * width
        integral += height

    return integral

# principal = input()
# rate = input()
# periods = input()

# print(f"Сумма кредита: {principal}")
# print(f"Ставка: {rate}")
# print(f"Период: {periods}")

principal = input("Сумма кредита: ")
rate = input("Ставка: ")
periods = input("Период: ")

percent = calculate_percent(principal, rate, periods)
total = principal + percent

print(f"Проценты: {percent}, Общая сумма: {total}")

