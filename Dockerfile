FROM python:3

RUN mkdir /code

WORKDIR /code
# Copy and install requirments first to leverage docker cache (Faster Build)
COPY requirements.txt . 
RUN pip install -r requirements.txt

COPY . /code/

WORKDIR /code/scalableapi

CMD python manage.py runserver 0.0.0.0:8000