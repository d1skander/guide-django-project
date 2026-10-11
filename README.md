![Алгоритм построение продукта](/docs/diagram.png)


> # Команды для запуска и настройки приложения
> > Скачивание uv
    1. Windows
        1. powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
        2. powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/0.13.0/install.ps1 | iex"
    2. Linux и MacOs
        1. curl -LsSf https://astral.sh/uv/install.sh | sh
        2. wget -qO- https://astral.sh/uv/install.sh | sh
        3. -LsSf https://astral.sh/uv/0.13.0/install.sh | sh


> > Команды django
    1. uv run guide_project/manage.py runserver
    2. uv run guide_project/manage.py makemigrations
    3. uv run guide_project/manage.py migrate
    4. uv run guide_project/manage.py createsuperuser


> # Полезные документации
1. [Uv doc][1]
2. [Django doc][2]


[1]: https://docs.astral.sh/uv/getting-started/installation/
[2]: https://www.djangoproject.com/start/overview/


**Данный проект был разработан для учебы :\)**