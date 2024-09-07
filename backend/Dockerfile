FROM python:3.12

COPY src/ .
COPY Pipfile .

RUN pip install pipenv
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy

ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=.

CMD ["pipenv", "run", "uvicorn", "start:app", "--port", "5000"]
