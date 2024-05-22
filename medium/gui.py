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
