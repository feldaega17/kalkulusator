FROM python:3.10-slim-buster

RUN pip3 install flask
COPY flag.txt /
RUN useradd -m quadra

WORKDIR /app
COPY app.py /app/
COPY templates/* /app/templates/
COPY themes/* /app/themes/

EXPOSE 5000

ENTRYPOINT ["python3", "app.py"]