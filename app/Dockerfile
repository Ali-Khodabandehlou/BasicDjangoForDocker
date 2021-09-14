FROM python:3.8.11-alpine

WORKDIR /usr/src/app


ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update\
    && apk add postgresql-dev gcc python3-dev musl-dev \
    # dependencies for pillow
    && apk add jpeg-dev zlib-dev

RUN pip install --upgrade pip
COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
