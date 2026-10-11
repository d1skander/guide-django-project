FROM python:3.12-slim


ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1


WORKDIR /app


COPY pyproject.toml

COPY . .

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/


RUN uv sync --locked


CMD ["uv", "run", "guide_project/manage.py", "runsever", "0.0.0.0:8000"]


EXPOSE 8000
#Docker еще не настроен.