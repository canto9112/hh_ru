import requests
import utils


def get_vacancies_page(vacancy, page):
    area_moscow = 1
    period = 30
    per_page_vacancies = 100

    params = {
        'text': f'Программист {vacancy}',
        'area': area_moscow,
        'period': period,
        'per_page': per_page_vacancies,
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
        all_vacancies, vacancies_found = get_all_vacancies_hh(language)
        all_salary = []
        salaries_sum = 0
        for vacancy in all_vacancies:
            if not vacancy['salary']:
                continue
            elif vacancy['salary']['currency'] != 'RUR':
                continue
            payment_from = vacancy['salary']['from']
            payment_to = vacancy['salary']['to']
            salary = utils.predict_rub_salary(payment_from, payment_to)
            if not salary:
                continue
            all_salary.append(salary)
            salaries_sum += salary
        vacancies_processed = len(all_salary)
        average_salary = salaries_sum / vacancies_processed
        average_salary_languages[language] = {
            'vacancies_found': vacancies_found,
            'vacancies_processed': vacancies_processed,
            'average_salary': int(average_salary)
        }
    return average_salary_languages


def get_all_vacancies_hh(language):
    all_vacancies = []
    page = 0
    pages_amount = 1
    while page < pages_amount:
        pages_amount, vacancies, vacancies_found = get_vacancies_page(language, page)
        all_vacancies.extend(vacancies)
        page += 1
    return all_vacancies, vacancies_found