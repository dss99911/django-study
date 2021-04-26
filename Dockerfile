FROM python:3.8-alpine

# Setting PYTHONUNBUFFERED to a non empty value ensures that the python output is sent straight to terminal (e.g. your container log) without being first buffered and that you can see the output of your application (e.g. django logs) in real time.
ENV PYTHONUNBUFFERED=1
ENV DJANGO_DATABASE_ENGINE=django.db.backends.sqlite3
ENV DJANGO_DATABASE_NAME=db.sqlite3
ENV DJANGO_DATABASE_USER=""
ENV DJANGO_DATABASE_PASSWORD=""
ENV DJANGO_DATABASE_HOST=""
ENV DJANGO_DATABASE_PORT=""
ENV DJANGO_ALLOWED_HOSTS=0.0.0.0
ENV DJANGO_ADMIN_NAME=admin
ENV DJANGO_ADMIN_PASSWORD=admin
ENV DJANGO_ADMIN_EMAIL=admin@admin.com
ENV DJANGO_DEBUG=False

ENV PATH="/scripts:${PATH}"
WORKDIR /code
COPY requirements.txt /code/

# install these libraries for installing uWSGI and psycopg2-binary(for using postgresql)
RUN apk add --update --no-cache --virtual .tmp postgresql-dev gcc libc-dev linux-headers python3-dev musl-dev

RUN pip install -r requirements.txt

# After install uWSGI, and pyscopg2-binary, remove not used virtual libraries
RUN apk del .tmp

# pyscopg2 needs libpq on runtime
RUN apk add --no-cache libpq
COPY . /code/
COPY scripts /scripts

RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D user
# -R recursively
RUN chown -R user:user /vol
# only owner have all permission. other user have read permission.
RUN chmod -R 755 /vol/web
USER user

ENTRYPOINT ["entrypoint.sh"]