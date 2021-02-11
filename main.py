import super_job
import hh_ru
import utils
import os
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()

    super_job_api_key = os.getenv('SUPER_JOB_KEY')

    languages = ['JavaScript', 'Java', 'Python', 'Ruby', 'PHP', 'Swift', 'C#', 'C', 'Go']

    hh_table_name = 'hh.ru'
    super_job_table_name = 'superJob'

    super_job_vacancies = super_job.get_average_salary_languages_superJob(languages, super_job_api_key)
    super_job_table = utils.get_terminal_table(super_job_vacancies, super_job_table_name)
    print(super_job_table)

    print('========')

    hh_ru_vacancies = hh_ru.get_average_salary_languages_hh(languages)
    hh_ru_table = utils.get_terminal_table(hh_ru_vacancies, hh_table_name)
    print(hh_ru_table)



