from terminaltables import AsciiTable


def get_terminaltables(dict, title):
    data = []
    data.append(['Язык программирования', 'Вакансий найдено', 'Вакансий обработано', 'Средняя зарплата' ])

    for vacancy in dict.items():
        language = vacancy[0]
        vacancies_found = vacancy[1]['vacancies_found']
        vacancies_processed = vacancy[1]['vacancies_processed']
        average_salary = vacancy[1]['average_salary']
        data.append([language, vacancies_found, vacancies_processed, average_salary])

    table = AsciiTable(data, title)
    print(table.table)

