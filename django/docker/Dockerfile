
FROM python:3

WORKDIR /django


# RUN apk update && \
#   apk add bash make gcc g++ postgresql-dev jpeg-dev zlib-dev && \
#   adduser django --shell /bin/bash --home /home/django --disabled-password
RUN apt-get update && \
  apt-get install bash make gcc g++ libmariadbclient-dev libssl-dev

# COPY requirements.txt requirements.txt

# RUN pip install -r requirements.txt

# RUN groupadd user && useradd --create-home --home-dir /home/user -g user user
# WORKDIR /home/user
#
# RUN pip install redis
#
# ENV CELERY_VERSION 4.0.2
#
# RUN pip install celery=="$CELERY_VERSION"
#
# RUN { \
# 	echo 'import os'; \
# 	echo "BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'amqp://')"; \
# } > celeryconfig.py
#
# # --link some-rabbit:rabbit "just works"
# ENV CELERY_BROKER_URL amqp://guest@rabbit
#
# USER user
# CMD ["celery", "worker"]



ENTRYPOINT ["docker/entrypoint.sh"]
# Говорим, какого пользователя мы хотим использовать в качестве пользователя по умолчанию.
# Будем использовать того, которого добавили ранее в третьей команде.

ENV PYTHONDONTWRITEBYTECODE=1
# Копируем все файлы из текущего контекста директории в рабочую директорию. Это нам понадобится, если мы решим
# запустить этот проект где то удаленно, пока мы просто будем поставлять файлы проекта с наших компьютеров напрямую.
COPY ./ ./
