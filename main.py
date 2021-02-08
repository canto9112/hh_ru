import super_job
import hh_ru
import utils


if __name__ =="__main__":
    languages = ['JavaScript', 'Java', 'Python', 'Ruby', 'PHP', 'Swift', 'C#', 'C', 'Go']
    hh_title_name = 'hh.ru'
    super_job_title_name = 'superJob'

    super_job = super_job.get_vacancies_dict(languages)
    hh_ru = hh_ru.get_vacancies_dict(languages)

    utils.get_terminaltables(hh_ru, hh_title_name)
    print('========')
    utils.get_terminaltables(super_job, super_job_title_name)