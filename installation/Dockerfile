FROM python:3
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SUPERUSER_PASSWORD=admin
WORKDIR /code
RUN python -m pip install --upgrade pip
RUN python -m pip install --upgrade Pillow
RUN python -m pip install --upgrade mysqlclient==1.3.12
RUN python -m pip install --upgrade django-mysql==2.2.0
RUN pip install Django==1.11.17
RUN git clone https://github.com/alazaralemayehu/django-project.git ecommerce
WORKDIR /code/ecommerce/src
