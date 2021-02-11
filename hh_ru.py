import requests
import utils
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
    response_json = response.json()
    pages_amount = response_json['pages']
    vacancies = response_json['items']
    found = response_json['found']
    return pages_amount, vacancies, found


def get_average_salary_languages_hh(languages):
    average_salary_languages = {}

    for language in languages:
        all_vacancies = []

        page = 0
        pages_amount = 1
        while page < pages_amount:
            pages_amount, vacancies, vacancies_found = get_first_page_vacancy(language, page)
            all_vacancies.extend(vacancies)
            page += 1

        all_salary = []
        sum_salarys = 0

        for vacancy in all_vacancies:
            if not vacancy['salary']:
                continue
            elif vacancy['salary']['currency'] != 'RUR':
                continue
            else:
                payment_from = vacancy['salary']['from']
                payment_to = vacancy['salary']['to']
                salary = utils.predict_rub_salary(payment_from, payment_to)
                if not salary:
                    continue
                else:
                    all_salary.append(salary)
                    sum_salarys += salary
        vacancies_processed = len(all_salary)
        average_salary = sum_salarys / vacancies_processed
        average_salary_languages.update({language:
                                        {'vacancies_found': vacancies_found,
                                         'vacancies_processed': vacancies_processed,
                                         'average_salary': int(average_salary)}})

    return average_salary_languages

