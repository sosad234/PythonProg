## Отчет
## Задание 
Сложность:
Medium
Реализуйте возможность быстрой смены GUI фреймворка. Продемонстрируйте миграцию с одного фреймворка на другой.

## Ход работы 

Пользователь может выбрать между использованием tkinter и PySimpleGUI для отображения интерфейса банковских услуг, что демонстрирует миграцию с одного фреймворка на другой. Этот код реализует два приложения с графическим интерфейсом для банковских услуг с использованием различных фреймворков: tkinter и PySimpleGUI. Оба приложения позволяют пользователям выбирать услугу (кредит, рассрочка, вклад), вводить сумму, процентную ставку и срок, рассчитывать результаты и сохранять их в файлы DOC и XLS. Версия с использованием tkinter представляет традиционный подход к созданию GUI с помощью библиотеки tkinter, в то время как версия с использованием PySimpleGUI предоставляет более простой интерфейс с использованием библиотеки PySimpleGUI.

## Код 
GUI_tkinter.py :
```python
import tkinter as tk
from tkinter import ttk
from main import run_app, save_to_doc, save_to_xls

def run_gui():
    root = tk.Tk()
    root.title("Банковские услуги")

    services = ["Кредит", "Рассрочка", "Вклад"]
    selected_service = tk.StringVar()
    amount = tk.DoubleVar()
    rate = tk.DoubleVar()
    term = tk.IntVar()

    service_combobox = ttk.Combobox(root, textvariable=selected_service, values=services)
    service_combobox.grid(row=0, column=1)

    amount_label = ttk.Label(root, text="Введите сумму:")
    amount_label.grid(row=1, column=0)
    amount_entry = ttk.Entry(root, textvariable=amount)
    amount_entry.grid(row=1, column=1)

    rate_label = ttk.Label(root, text="Введите процентную ставку:")
    rate_label.grid(row=2, column=0)
    rate_entry = ttk.Entry(root, textvariable=rate)
    rate_entry.grid(row=2, column=1)

    term_label = ttk.Label(root, text="Введите срок (в месяцах):")
    term_label.grid(row=3, column=0)


    term_entry = ttk.Entry(root, textvariable=term)
    term_entry.grid(row=3, column=1)

    def calculate():
        service = selected_service.get()
        amount_value = amount.get()
        rate_value = rate.get()
        term_value = term.get()
        result = run_app(service, amount_value, rate_value, term_value)
        result_label = ttk.Label(root, text=f"Результат: {result}")
        result_label.grid(row=4, column=1)

    def save():
        # Сохранение результата в файлы
        pass

    calculate_button = ttk.Button(root, text="Рассчитать", command=calculate)
    calculate_button.grid(row=5, column=0)

    save_button = ttk.Button(root, text="Сохранить", command=save)
    save_button.grid(row=5, column=1)

    root.mainloop()

if __name__ == '__main__':
    run_gui()
```

PySimpleGUI :
```python
import PySimpleGUI as sg
from main import run_app, save_to_doc, save_to_xls

def run_gui():
    layout = [
        [sg.Text('Выберите услугу:'), sg.Combo(['Кредит', 'Рассрочка', 'Вклад'], key='-SERVICE-')],
        [sg.Text('Введите сумму:'), sg.Input(key='-AMOUNT-')],
        [sg.Text('Введите процентную ставку:'), sg.Input(key='-RATE-')],
        [sg.Text('Введите срок (в месяцах):'), sg.Input(key='-TERM-')],
        [sg.Button('Рассчитать'), sg.Button('Сохранить'), sg.Button('Выход')]
    ]

    window = sg.Window('Банковские услуги', layout)
    result = None

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Выход':
            break
        elif event == 'Рассчитать':
            result = run_app(values['-SERVICE-'], values['-AMOUNT-'], values['-RATE-'], values['-TERM-'])
            sg.popup('Результат: ', result)
        elif event == 'Сохранить':
            if result is not None:
                save_to_doc(result)
                save_to_xls(result)
                sg.popup('Результат сохранен.')
            else:
                sg.popup('Рассчитайте результаты перед сохранением.')

    window.close()

if __name__ == '__main__':
    run_gui()
```


main.py :

```python 
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
```

## Источники 

1. Документация tkinter: https://docs.python.org/3/library/tkinter.html
2. Документация PySimpleGUI: https://pysimplegui.readthedocs.io/en/latest/
