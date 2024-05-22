import PySimpleGUI as sg
from docx import Document
from openpyxl import Workbook
from abc import ABC, abstractmethod

class BankService(ABC):
    def __init__(self, amount, rate, term):
        self._amount = amount
        self._rate = rate
        self._term = term

    @abstractmethod
    def calculate(self):
        pass

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        self._rate = value

    @property
    def term(self):
        return self._term

    @term.setter
    def term(self, value):
        self._term = value

class CreditService(BankService):
    def calculate(self):
        payment = self.amount / self.term
        return f"Ежемесячный платеж: {payment}"

    def __str__(self):
        return "Кредитный сервис"

class InstallmentService(BankService):
    def calculate(self):
        payment = self.amount / self.term
        return f"Ежемесячный платеж: {payment}"

    def __str__(self):
        return "Сервис рассрочки"

class DepositService(BankService):
    def calculate(self):
        return "Вклад не предполагает ежемесячных платежей"

    def __str__(self):
        return "Сервис вкладов"

def save_to_doc(result):
    doc = Document()
    doc.add_paragraph(f'Результат: {result}')
    doc.save('результат.docx')

def save_to_xls(result):
    wb = Workbook()
    ws = wb.active
    ws['A1'] = 'Результат:'
    ws['B1'] = result
    wb.save('результат.xlsx')

layout = [
    [sg.Text('Выберите услугу:'), sg.Combo(['Кредит', 'Рассрочка', 'Вклад'], key='-SERVICE-')],
    [sg.Text('Введите сумму:'), sg.Input(key='-AMOUNT-')],
    [sg.Text('Введите процентную ставку:'), sg.Input(key='-RATE-')],
    [sg.Text('Введите срок (в месяцах):'), sg.Input(key='-TERM-')],
    [sg.Button('Рассчитать'), sg.Button('Сохранить'), sg.Button('Выход')]
]

window = sg.Window('Банковские услуги', layout)
service = None

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Выход':
        break
    elif event == 'Рассчитать':
        if values['-SERVICE-'] == 'Кредит':
            service = CreditService(float(values['-AMOUNT-']), float(values['-RATE-']), int(values['-TERM-']))
        elif values['-SERVICE-'] == 'Рассрочка':
            service = InstallmentService(float(values['-AMOUNT-']), float(values['-RATE-']), int(values['-TERM-']))
        elif values['-SERVICE-'] == 'Вклад':
            service = DepositService(float(values['-AMOUNT-']), float(values['-RATE-']), int(values['-TERM-']))
        result = service.calculate()
        sg.popup('Результат: ', result)
    elif event == 'Сохранить':
        if service is not None:
            save_to_doc(result)
            save_to_xls(result)
            sg.popup('Результат сохранен.')
        else:
            sg.popup('Рассчитайте результаты перед сохранением.')
window.close()

