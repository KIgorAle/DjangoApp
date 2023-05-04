# DjangoApp - сайт на Django написанный для выполнения тестового задания.

## Задание:
Нужно сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:
1) Меню реализовано через template tag.
2) Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
3) Хранится в БД.
4) Редактируется в стандартной админке Django.
5) Активный пункт меню определяется исходя из URL текущей страницы.
6) Меню на одной странице может быть несколько. Они определяются по названию.
7) При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
8) На отрисовку каждого меню требуется ровно 1 запрос к БД.
9) Нужен django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию: {% draw_menu 'main_menu' %}
10) При выполнении задания из библиотек следует использовать только Django и стандартную библиотеку Python.
 
 ## Чтобы поднять сайт (есть не один способ, я опишу свой):
 1) Скачиваем весь код, открываем папку с кодом в PyCharm 2021.1 (Community Edition), выбираем интерпритатор Python 3.9.
 2) Устанавливем зависимости из requirements.txt (по сути там только Django 4.2): pip install -r requirements.txt
 3) Запускаем сервер: python manage.py runserver
 4) Готово. Открываем сайт по ссылке http://127.0.0.1:8000/
 5) Если требуется админка, открываем её по ссылке http://127.0.0.1:8000/admin/ - логин "SU_DjaDB", пароль "pasS123#&_".
 6) Проверяем работоспособность приложения. Дизайн простой, но от меня только требовалось показать два разных правильно работающих меню на странице, css минималистично отвечает этому требованию.

## Демонстрация:
1) Главная страница, единственная куда я поместил два меню:
![1](https://user-images.githubusercontent.com/25643872/236263319-cf4179b8-9c40-44b1-9da8-796aa4054ebb.png)

2) Страница местоположения, содержит одно меню (main_menu):
![2](https://user-images.githubusercontent.com/25643872/236263323-7c091331-4daf-48f2-9a61-c382617c6ca0.png)

