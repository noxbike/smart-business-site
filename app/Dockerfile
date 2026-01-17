FROM --platform=$BUILDPLATFORM python:3.11 AS builder
WORKDIR /app
EXPOSE 8000
COPY requirements.txt /app/
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app
CMD [ "python3", "manage.py", "runserver" , "0.0.0.0:8000"]