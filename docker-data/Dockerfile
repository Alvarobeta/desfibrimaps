FROM python:3.7
LABEL maintainer="alvaromr91@gmail.com"

COPY ./ /app

WORKDIR /app

RUN python -m pip install --upgrade pip

RUN pip install mysqlclient==1.4.4 pymysql
RUN pip install -r requirements-dev.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]