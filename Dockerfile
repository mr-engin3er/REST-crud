FROM python:3.10.0a6-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
WORKDIR /web
COPY ./requirements.pip .
RUN pip install -r requirements.pip
COPY . .
# run entrypoint.sh
ENTRYPOINT ["sh","/web/entry-point.sh"]

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "REST_crud.wsgi"]