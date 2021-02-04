import requests
from pprint import pprint

def get_first_page_vacancy(vacancy, page):
    params = {
        'text': f'Программист {vacancy}',
        'area': 1,
        'period': 30,
        'per_page': 100,
        'page': page
    }
    response = requests.get('https://api.hh.ru/vacancies', params=params)
    response.raise_for_status()
    return response.json()


def predict_rub_salary(salary):
    average = []
    for sal in salary:
        if sal is None:
            None
        elif sal['currency'] != 'RUR':
            None
        elif sal['currency'] == 'RUR':
            from_salary = sal['from']
            to_salary = sal['to']
            if from_salary is None and to_salary is not None:
                average_salary = to_salary * 0.8
                average.append(int(average_salary))
            elif from_salary is not None and to_salary is None:
                average_salary = from_salary * 1.2
                average.append(int(average_salary))
            else:
                average_salary = (from_salary + to_salary) / 2
                average.append(int(average_salary))

    vacancies_processed = len(average)
    sum_salary = 0
    for selary in average:
        sum_salary += selary
    average_salarys = sum_salary / vacancies_processed

    return vacancies_processed, int(average_salarys)


if __name__ == '__main__':
    # name_vacancies = ['JavaScript', 'Java', 'Python', 'Ruby', 'PHP',
    #                   'C++', 'Swift', 'C#', 'C', 'Go']
    name_vacancies = ['C', 'Go', 'C#', 'PHP', 'C++', 'Swift']
    number_page = 0

    vacancies = []
    dict_vacations = {}
    for vacancy in name_vacancies:
        first_page_response = get_first_page_vacancy(vacancy, number_page)

        vacancies_found = first_page_response['found']
        pages = first_page_response['pages']
        firs_page_vacancies = first_page_response['items']

        for page in range(2, pages + 1):
            vacancies += get_first_page_vacancy(vacancy, page)['items']
            if page == 19:
                break

        salary = []
        for sal in vacancies:
            salary.append(sal['salary'])

        vacancies_processed, average_salarys = predict_rub_salary(salary)
        dict_vacations.update({vacancy:
                                   {'Найдено вакансий': vacancies_found,
                                    'Обработано вакансий': vacancies_processed,
                                    'Средняя ЗП': average_salarys}})

    pprint(dict_vacations)




