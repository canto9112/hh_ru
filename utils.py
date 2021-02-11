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
