![Алгоритм построение продукта](/docs/diagram.png)


> # Команды для запуска и настройки приложения
> > Скачивание uv
> > > Windows
> > > > powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
> > > > > > > > powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/0.13.0/install.ps1 | iex"
> > > Linux и MacOs
> > > > curl -LsSf https://astral.sh/uv/install.sh | sh
> > > > wget -qO- https://astral.sh/uv/install.sh | sh
> > > > curl -LsSf https://astral.sh/uv/0.13.0/install.sh | sh


> > Команды django
> > > > uv run guide_project/manage.py runserver
> > > > uv run guide_project/manage.py makemigrations
> > > > uv run guide_project/manage.py migrate
> > > > uv run guide_project/manage.py createsuperuser


> # Полезные документации
> > [Uv doc][1]
> > [Django doc][2]


[1]: https://docs.astral.sh/uv/getting-started/installation/
[2]: https://www.djangoproject.com/start/overview/


**Данный проект был разработан для учебы :\)**