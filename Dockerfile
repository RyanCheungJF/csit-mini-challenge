FROM python:3.10

WORKDIR /app

ARG DBURI
ENV DBURI ${DBURI}

COPY pyproject.toml pyproject.toml

ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY . .

RUN ls

EXPOSE 8080

CMD  python3 app/main.py
