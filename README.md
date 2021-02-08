# Сравниваем вакансии программистов

Скрипт ```main.py``` выводит таблицу для сравнивнения вакансий программистов на разных языках с сайта HeadHunter и SuperJob в регионе - Москва.

### Как установить

У вас уже должен быть установлен Python 3. Если его нет, то установите.
Так же нужно установить необходимые пакеты:
```
pip3 install -r requirements.txt
```

### Как пользоваться скриптом

Для работы скрипта нужно создать файл ```.env``` в директории где лежит скрипт. Также нужно вставить
API ключ SuperJob. Чтобы использовать все методы API, необходимо [зарегистрировать](https://api.superjob.ru/register) приложение. Вставьте ваш API ключ SuperJob  ```.env```:
```
SUPER_JOB_KEY='v3.r.133629723.03e22945a1fc91aa0b1b21b757d831cb55d505cf.3ed772de1bb43c4a32e23a2fa89e349603cdea62'
```

Для запуска скрипта вам необходимо запустить командную строку и перейти в каталог со скриптом:
```
[путь_до_файла] python3 main.py 
```
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).