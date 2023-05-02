FROM python:3.11.0-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update && apt-get -y install default-libmysqlclient-dev python3-dev gcc libc-dev netcat

WORKDIR /apps
COPY . /apps

RUN echo "psycopg2-binary" >> /apps/requirements.txt
RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -r /apps/requirements.txt

RUN sed -i 's/\r$//g' /apps/entrypoint.sh
RUN chmod +x /apps/entrypoint.sh

ENTRYPOINT ["sh", "/apps/entrypoint.sh"]

