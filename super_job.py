import requests


def get_first_page_vacancy(vacancy):
    url = '	https://api.superjob.ru/2.0/vacancies/'
    headers = {'X-Api-App-Id':
                   'v3.r.133629723.03e22945a1fc91aa0b1b21b757d831cb55d504cf.3ed772de0bb43c4a32e23a2fa89e219603cdea62'}
    params = {
        'count': 100,
        'keyword': f'Программист {vacancy}',
        'town': 4,
        'catalogues': 33
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()


def predict_rub_salary_for_superJob(vacancy):
    payment_from = vacancy['payment_from']
    payment_to = vacancy['payment_to']

    if payment_from == 0 and payment_to == 0:
        return None
    elif payment_from == 0 and payment_to != 0:
        average_salary = payment_to * 0.8
    elif payment_from != 0 and payment_to == 0:
        average_salary = payment_from * 1.2
    else:
        average_salary = (payment_from + payment_to) / 2
    return average_salary


def get_vacancies_dict(languages):
    average_salary_languages = {}

    for language in languages:
        first_page_vacancy = get_first_page_vacancy(language)
        total = first_page_vacancy['total']

        all_salary = []
        sum_salarys = 0
        for number_vacancy in range(0, total):
            if number_vacancy < 100:
                vacancy = first_page_vacancy['objects'][number_vacancy]
                salary = predict_rub_salary_for_superJob(vacancy)
                if salary is None:
                    pass
                else:
                    all_salary.append(salary)
                    sum_salarys += salary

        vacancies_processed = len(all_salary)
        average_salary = sum_salarys / vacancies_processed

        average_salary_languages.update({language:
                                        {'vacancies_found': total,
                                         'vacancies_processed': vacancies_processed,
                                         'average_salary': int(average_salary)}})
    return average_salary_languages

