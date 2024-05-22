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