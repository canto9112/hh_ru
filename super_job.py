import requests
import utils


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


def get_average_salary_languages_superJob(languages, api_key):
    average_salary_languages = {}
    for language in languages:
        all_vacancies, total = get_all_vacancies_superJob(language, api_key)
        all_salarys = []
        salaries_sum = 0
        for vacancy in all_vacancies:
            payment_from = vacancy['payment_from']
            payment_to = vacancy['payment_to']
            salary = utils.predict_rub_salary(payment_from, payment_to)
            if not salary:
                continue
            all_salarys.append(salary)
            salaries_sum += salary
        vacancies_processed = len(all_salarys)
        average_salary = salaries_sum / vacancies_processed
        average_salary_languages.update({language:
                                        {'vacancies_found': total,
                                         'vacancies_processed': vacancies_processed,
                                         'average_salary': int(average_salary)}})
    return average_salary_languages


def get_all_vacancies_superJob(language, api_key):
    all_vacancies = []
    more = True
    page = 0
    while more:
        page_response = get_vacancies(language, api_key, page)
        all_vacancies.extend(page_response['objects'])
        total = page_response['total']
        more = page_response['more']
        page += 1
    return all_vacancies, total