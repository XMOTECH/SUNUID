FROM python:3.13-slim

WORKDIR /code

# Copier uniquement les fichiers de dépendances
COPY pyproject.toml poetry.lock* /code/

# Installer Poetry et les dépendances
RUN pip install poetry && poetry install --no-root

# Copier le code applicatif
COPY ./app /code/app

# Lancer avec poetry run pour être sûr que uvicorn est trouvé
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
