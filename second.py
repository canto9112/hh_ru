import requests
from pprint import pprint
from time import sleep


def get_vacancies_found(url, vacancy, area, period):
    params = {
        'text': f'Программист {vacancy}',
        'area': area,
        'period': period
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    vacancies_found = response.json()['found']
    return vacancies_found


def get_salary(url, vacancy, area, period, page, per_page):
    params = {
        'text': f'Программист {vacancy}',
        'area': area,
        'period': period,
        'page': page,
        'per_page': per_page
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    salarys = []
    for vacancy in range(page, per_page):
        salary = response.json()['items'][vacancy]['salary']
        salarys.append(salary)
    return salarys


def predict_rub_salary(salarys):
    average = []
    for salary in salarys:
        if salary is None:
            None
        elif salary['currency'] != 'RUR':
            None
        elif salary['currency'] == 'RUR':
            from_salary = salary['from']
            to_salary = salary['to']
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


def get_numbers_first_page(url, vacancy, per_page, area, period):
    pages = []
    params = {'text': vacancy,
              'area': area,
              'period': period,
              'per_page': per_page}
    page = 0
    pages_number = 1
    while page < pages_number:
        response = requests.get(url, params=params)
        response.raise_for_status()
        pages_number = response.json()["pages"]
        page += 1
        pages.append(page)
    return pages


def get_dict_vacancys(vacancies, url, area, period, page, per_page):
    dict_vacations = {}
    for vacancy in vacancies:
        salarys = get_salary(url, vacancy, area, period, page, per_page)
        vacancies_processed, average_salary = predict_rub_salary(salarys)
        vacancies_found = get_vacancies_found(url, vacancy, area, period)
        dict_vacations.update({vacancy:
                     {'vacancies_found': vacancies_found,
                      'vacancies_processed': vacancies_processed,
                      'average_salary': average_salary}})
    pprint(dict_vacations)
    return dict_vacations


def get_all_salarys_list(url, vacancy, per_page, area, period):
    vacancy_pages = get_numbers_first_page(url, vacancy, per_page, area, period)
    salarys = []
    for pages in vacancy_pages:
        if pages < len(vacancy_pages) - 1:
            salary = get_salary(api_url, vacancy, area, period, pages, per_page)
            salarys.append(salary)
        else:
            pass
    pprint(salarys)
    return salarys

if __name__ == '__main__':
    vacancies = ['JavaScript', 'Java', 'Python']
    api_url = 'https://api.hh.ru/vacancies'
    area = 1
    period = 30
    page = 0
    per_page = 100

    # get_dict_vacancys(vacancies, api_url, area, period, page, per_page)
    get_all_salarys_list(api_url, 'Python', per_page, area, period)





# salarys = get_all_salarys_list(api_url, 'Python', per_page, area, period)
# average = []
# for salary in salarys:
#     for sal in salary:
#         if sal is None:
#             None
#         elif sal['currency'] != 'RUR':
#             None
#         elif sal['currency'] == 'RUR':
#             from_salary = sal['from']
#             to_salary = sal['to']
#             if from_salary is None and to_salary is not None:
#                 average_salary = to_salary * 0.8
#                 average.append(int(average_salary))
#             elif from_salary is not None and to_salary is None:
#                 average_salary = from_salary * 1.2
#                 average.append(int(average_salary))
#             else:
#                 average_salary = (from_salary + to_salary) / 2
#                 average.append(int(average_salary))
#     vacancies_processed = len(average)
#     sum_salary = 0
#     for selary in average:
#         sum_salary += selary
#     average_salarys = sum_salary / vacancies_processed
#
# print('Обработано объявлений -', vacancies_processed)
# print('Программист Python', int(average_salarys))









