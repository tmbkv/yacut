# YaCut
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/-Scrapy-blue)](https://flask.palletsprojects.com/en/2.3.x/)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-blue)](https://www.sqlalchemy.org/)
## Сервис укорачивания ссылок YaCut, разработанный с помощью фреймворков Flask и REST API на Flask. В качестве ORM использовался SQLAchemy.
Сервис YaCut ассоциирует длинную пользовательскую ссылку с короткой.
Короткая ссылка предоставляется следующими вариантами:
1. Пользователь вводит свой вариант короткой ссылки, состоящей из не более чем 6 допустимых символов;
2. Пользователь может сгенерировать короткий вариант ссылки с помощью сервиса YaCut.
### Перед использованием
1. Клонируйте репозиторий на локальный ПК:
```
git clone git@github.com:tmbkv/yacut.git
```

2. В корневой папке создайте виртуальное окружение и установите зависимости:
```
python -m venv venv
```
```
pip install -r requirements.txt
```
3. Запустите сервис командой:
```
flask run
```
4. Протестируйте сервис на локальном сервере http://127.0.0.1:5000/

### Автор
- [Константин Тамбов](https://github.com/tmbkv "GitHub аккаунт")
