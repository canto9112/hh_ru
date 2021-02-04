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
    # name_vacancies = ['JavaScript', 'Java', 'Python', 'Ruby', 'PHP',
    #                   'C++', 'Swift', 'C#', 'C', 'Go']
    name_vacancies = ['JavaScript', 'Java', 'Python', 'Ruby', 'PHP',
                      'Swift', 'C#', 'C', 'Go']
    number_page = 0


    dict_vacations = {}
    for vacancy in name_vacancies:

        first_page_response = get_first_page_vacancy(vacancy, number_page)

        vacancies_found = first_page_response['found']
        pages = first_page_response['pages']
        firs_page_vacancies = first_page_response['items']

        vacancies = []
        for page in range(2, pages + 1):
            vacancies += get_first_page_vacancy(vacancy, page)['items']
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
        # print(sum_salarys)
        vacancies_processed = len(all_salary)
        print('Обработано вакансий', vacancies_processed)
        average_salary = sum_salarys / vacancies_processed
        print('Средняя Зп', int(average_salary))


    #         salary.append(sal['salary'])
    #
    #     vacancies_processed, average_salarys = predict_rub_salary(salary)
    #     dict_vacations.update({vacancy:
    #                                {'Найдено вакансий': vacancies_found,
    #                                 'Обработано вакансий': vacancies_processed,
    #                                 'Средняя ЗП': average_salarys}})
    #
    # pprint(dict_vacations)




