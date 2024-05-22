# Вклад 
# a - исходная сумма, y - срок в годах, p - процентная ставка
def task(a,y,p):
    for _ in range(y):
        a = (1+p/100)*a
    return a

a = str(input("исходная сумма: "))
y = str(input("срок в годах: "))
p = str(input("процентная ставка: "))

task(a, y, p)
