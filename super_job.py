import requests
from pprint import pprint


def get_vacancies(vacancy, api_key, page):
    url = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {'X-Api-App-Id': api_key}
    params = {
        'count': 100,
        'page': page,
        'keyword': f'Программист {vacancy}',
        'town': 4,
        'catalogues': 33
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()


def predict_rub_salary_for_superJob(vacancy, total):
    for number_vacancy in range(0, total):

        payment_from = vacancy['objects'][number_vacancy]['payment_from']
        payment_to = vacancy['objects'][number_vacancy]['payment_to']

        if payment_from == 0 and payment_to == 0:
            return None
        elif payment_from == 0 and payment_to != 0:
            average_salary = payment_to * 0.8
        elif payment_from != 0 and payment_to == 0:
            average_salary = payment_from * 1.2
        else:
            average_salary = (payment_from + payment_to) / 2
        return average_salary


def get_average_salary_languages_superJob(languages, api_key):
    average_salary_languages = {}

    for language in languages:
        all_vacancies = get_all_vacancies_superJob(language, api_key)
        total = all_vacancies[0]['total']

        all_salary = []
        sum_salarys = 0
        for vacancy in all_vacancies:
            salary = predict_rub_salary_for_superJob(vacancy, total)
            if salary is None:
                pass
            else:
                all_salary.append(salary)
                sum_salarys += salary
        print(all_salary)
        vacancies_processed = len(all_salary)
        average_salary = sum_salarys / vacancies_processed

        average_salary_languages.update({language:
                                        {'vacancies_found': total,
                                         'vacancies_processed': vacancies_processed,
                                         'average_salary': int(average_salary)}})
    print(average_salary_languages)
    return average_salary_languages


def get_all_vacancies_superJob(language, api_key):
    all_vacancies = []
    more = True
    page = 0
    while more:
        first_page_vacancy = get_vacancies(language, api_key, page)
        all_vacancies.append(first_page_vacancy)
        more = first_page_vacancy['more']
        page += 1
    return all_vacancies