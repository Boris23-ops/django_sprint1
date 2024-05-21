# Blogicum
Реализация социальной сети **Blogicum**. 

Основные возможности:
- чтение публикаций. 

Проект является учебным. Основная польза в приобретении понимания реализации проекта через фреймворк `Django`, с использованием: 
- основ развёртывания `Django` проекта;
- установки приложений и их регистрация;
- настройки локализации и часового пояса;
- инструментов описания маршрутов `URL`;
- инструментов создания `html` шаблонов всех страниц в отдельной директории `templates`;
- подключения `css` файла, иконок в виде статических материалов из отдельной директории `static` ; 
- `view-функций`, позволяющих рендерить страницы, на основе `base.html`;
- интегрированного в `Django` сервера, через который доступен текущий продукт.

<br>

## Технологический стек:
- [Python 3.11.5](https://docs.python.org/release/3.11.5/)
- [Django 3.2.16](https://docs.djangoproject.com/en/3.2/)
- [Pytest 7.4.2](https://docs.pytest.org/en/7.4.x/)

<br>

## Развёртывание проекта:
+ Клонировать репозиторий и перейти в него в командной строке:
```shell script
git clone git@github.com:Boris23-ops/django_sprint1.git
```

```shell script
cd django_sprint1/
```

+ Cоздать и активировать виртуальное окружение (Windows/Bash):
```shell script
python -m venv venv
```

```shell script
source venv/Scripts/activate
```

+ Установить зависимости из файла requirements.txt:
```shell script
python -m pip install --upgrade pip
```

```shell script
pip install -r requirements.txt
```

+ Перейти в директорию с manage.py:
```shell script
cd blogicum/
```

+ Выполнить миграции:
```shell script
python manage.py migrate
```

+ Запустить проект:
```shell script
python manage.py runserver
```

<br>

## Просмотр контента:
Перейти по адресу http://127.0.0.1:8000/. На данный момент доступно несколько записей, загруженных непосредственно во view-функцию. 

<br>

## Тестирование проекта:
Тестирование реализовано с использованием библиотеки Pytest. 

+ Запустить тесты из основной директории проекта:
```shell script
pytest
```

<br>

### Автор
_[Короткиян Борис](https://github.com/Boris23-ops)_<br>