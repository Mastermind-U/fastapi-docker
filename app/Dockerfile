FROM duffn/python-poetry:3.10-buster

WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi
COPY app /app
