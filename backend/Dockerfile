FROM python:3.11

COPY public/ public/
COPY src/ src/
COPY Pipfile .
COPY docker.env .env

RUN pip install pipenv
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy

ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=.

CMD ["pipenv", "run", "uvicorn", "src.start:app", "--port", "5000", "--host", "0.0.0.0"]
