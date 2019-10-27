FROM python:3

ENV PYTHONBUFFERED 1

WORKDIR /install
RUN apt-get update && apt-get install --yes libgdal-dev libjpeg-dev

COPY requirements_docker.txt .

RUN pip install -r requirements_docker.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
