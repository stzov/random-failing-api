FROM python:3.7-slim

ENV TZ=UTC
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN useradd --create-home app
WORKDIR /home/app
USER app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5678
ENTRYPOINT ["bash", "gunicorn.sh"]

