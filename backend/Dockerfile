FROM python:3.10.12-alpine3.17


ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

WORKDIR /code
COPY . /code
EXPOSE 8000:8000

# runserver
# CMD ["python", "manage.py", "runserver", "8000"]