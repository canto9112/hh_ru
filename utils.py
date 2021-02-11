from terminaltables import AsciiTable


def get_terminal_table(vacancies_dict, title):
    data = [['Язык программирования', 'Вакансий найдено', 'Вакансий обработано', 'Средняя зарплата']]
    for language, value, in vacancies_dict.items():
        data.append([language,
                     value['vacancies_found'],
                     value['vacancies_processed'],
                     value['average_salary']])
    table = AsciiTable(data, title)
    return table.table


def predict_rub_salary(payment_from, payment_to):
    if payment_from is None and payment_to is not None:
        average_salary = payment_to * 0.8
    elif payment_from is not None and payment_to is None:
        average_salary = payment_from * 1.2
    else:
        average_salary = (payment_from + payment_to) / 2
    return average_salary
