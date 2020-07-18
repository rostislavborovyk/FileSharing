FROM python:3

RUN pip install poetry
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

#EXPOSE 8000
EXPOSE ${PORT}

RUN chmod +x prod.sh
ENTRYPOINT ["./prod.sh"]
