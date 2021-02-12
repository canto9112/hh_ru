from terminaltables import AsciiTable


def get_terminal_table(vacancies_dict, title):
    data = [['Язык программирования', 'Вакансий найдено', 'Вакансий обработано', 'Средняя зарплата']]
    for language, statistics, in vacancies_dict.items():
        data.append([language,
                     statistics['vacancies_found'],
                     statistics['vacancies_processed'],
                     statistics['average_salary']])
    table = AsciiTable(data, title)
    return table.table


def predict_rub_salary(payment_from, payment_to):
    if payment_from:
        average_salary = payment_from * 1.2
        return average_salary
    elif payment_to:
        average_salary = payment_to * 0.8
        return average_salary
    elif payment_from and payment_to:
        return None
    else:
        average_salary = (payment_from + payment_to) / 2
        return average_salary