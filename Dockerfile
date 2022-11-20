FROM python:3.10.7-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code

WORKDIR /code

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . /code/

#RUN python manage.py collectstatic --noinput

#EXPOSE 8000

# replace demo.wsgi with <project_name>.wsgi
#CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "CarProject.wsgi"]
