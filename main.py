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


def predict_rub_salary(vacancy):
    salary = vacancy['salary']

    if salary is None:
        None
    elif salary['currency'] != 'RUR':
        None
    elif salary['currency'] == 'RUR':
        from_salary = salary['from']
        to_salary = salary['to']
        if from_salary is None and to_salary is not None:
            average_salary = to_salary * 0.8
        elif from_salary is not None and to_salary is None:
            average_salary = from_salary * 1.2
        else:
            average_salary = (from_salary + to_salary) / 2
        return average_salary


if __name__ == '__main__':

    languages = ['JavaScript', 'Java', 'Python', 'Ruby', 'PHP', 'Swift', 'C#', 'C', 'Go']
    number_page = 0

    average_salary_languages = {}
    for language in languages:
        first_page_response = get_first_page_vacancy(language, number_page)
        vacancies_found = first_page_response['found']
        pages = first_page_response['pages']
        firs_page_vacancies = first_page_response['items']

        vacancies = []
        for page in range(2, pages + 1):
            vacancies += get_first_page_vacancy(language, page)['items']
            if page == 19:
                break

        all_salary = []
        sum_salarys = 0
        for vacancy in vacancies:
            salary = predict_rub_salary(vacancy)
            if salary is None:
                pass
            else:
                all_salary.append(salary)
                sum_salarys += salary

        vacancies_processed = len(all_salary)
        average_salary = sum_salarys / vacancies_processed

        average_salary_languages.update({language:
                                        {'Найдено вакансий': vacancies_found,
                                         'Обработано вакансий': vacancies_processed,
                                         'Средняя ЗП': int(average_salary)}})

    pprint(average_salary_languages)




