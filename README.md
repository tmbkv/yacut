# Scrapy Parser PEP 
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/)
[![Scrapy](https://img.shields.io/badge/-Scrapy-blue)](https://docs.scrapy.org/en/latest/index.html)
## Проект асинхронного парсинга документов PEP с помощью фреймворка Scrapy 
Парсинг документов PEP осуществляется с сайта **https://peps.python.org/**

Парсер выводит информацию в два файла:
1. В первый файл список всех PEP: номер, названия и статус;
2. Во второй количество всех статусов и количество каждого статуса по отдельности.
### Перед использованием
1. Клонируйте репозиторий на локальный ПК:
```
git clone git@github.com:tmbkv/scrapy_parser_pep.git
```

2. В корневой папке создайте виртуальное окружение и установите зависимости:
```
python -m venv venv
```
```
pip install -r requirements.txt
```
3. Запустите парсер командой:
```
scrapy crawl pep
```
4. Результат отобразится в файлах в папке 'results' корневой директории.

### Автор
- [Константин Тамбов](https://github.com/tmbkv "GitHub аккаунт")
