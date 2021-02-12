from terminaltables import AsciiTable


def get_terminal_table(vacancies, title):
    data = [['Язык программирования', 'Вакансий найдено', 'Вакансий обработано', 'Средняя зарплата']]
    for language, statistics, in vacancies.items():
        data.append([language,
                     statistics['vacancies_found'],
                     statistics['vacancies_processed'],
                     statistics['average_salary']])
    table = AsciiTable(data, title)
    return table.table


def predict_rub_salary(payment_from, payment_to):
    if payment_from:
        return payment_from * 1.2
    elif payment_to:
        return payment_to * 0.8
    elif payment_from and payment_to:
        return None
    else:
        return (payment_from + payment_to) / 2